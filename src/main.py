import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware

from fb_scraper import scraper

from schemas import FBPAGE as fbPageSchema
from models import FBPAGE as fbPageModel

from credentials import credential_fb

import os
from dotenv import load_dotenv

#load db url from env
load_dotenv('.env')

#init app
app = FastAPI()

#cross origin handler
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#session init
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])



#routes
@app.get("/")
async def root():
    return {"Message": "Hello ELYADATA!"}


@app.post('/scrape-page/')
async def page(page_name : str = "avengers" , page_scroll_cnt : int = 2):
    try : 
        email , password = credential_fb()
        posts = scraper(page_name,page_scroll_cnt,email,password)
        for data in posts:
            db_page = fbPageModel(
                post_url=data["post_url"],
                text=data["text"],
                time=data["time"],
                image=data["image"],
                likes=data["likes"],
                comments=data["comments"],
                shares=data["shares"]
            )
            db.session.add(db_page)
            db.session.commit()
        return "Success"
    except Exception as e :
        return str(e)

@app.get('/pages')
async def index():
    pages = db.session.query(fbPageModel).all()
    return pages


@app.get('/check-db')
async def index():
    cnt = db.session.query(fbPageModel).count()
    return {"row count" : cnt}

