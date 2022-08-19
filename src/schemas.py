# build a schema using pydantic
from pydantic import BaseModel

class FBPAGE(BaseModel):
    post_url = str
    text = str
    time = str
    image = str
    likes = int
    comments = int
    shares = int

    class Config:
        orm_mode = True