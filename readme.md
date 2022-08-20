#How to run:

##    - docker-compose up --build

##    - access through URL: localhost:8000

#Available routes:

/?page_name="public page name"&page_scroll_cnt="how many pages to scroll through" : scrape a public page and save data to postgresql DB
!the bigger the "page_scroll_cnt" the more times it will take for scraping to be executed and saved in DB

/pages : view all scrapped pages

/check-db : check how many rows we have in the table (for checking if the API works)


#Remarks
!no need to provide credentials, I have already created a test account

!env.py file in alembic folder was altered according to app's needs