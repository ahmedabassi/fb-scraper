#    How to run:

##    -1- `docker-compose up -d --build` 

##    -2- `docker exec -it <web_container_name> bash -c "./tuto.sh"` : for futher instruction on how to use the App

##    -3- access main page through URL: localhost:8000

##    -4- access APIs through URL: localhost:8000/docs


#Available routes:

/scrape-page?page_name="public page name"&page_scroll_cnt="how many pages to scroll through" : scrape a public page and save data to postgresql DB
!the bigger the "page_scroll_cnt" the more times it will take for scraping to be executed and saved in DB

/pages : view all scrapped pages

/check-db : check how many rows we have in the table (for checking if the API works)


#Remarks
!no need to provide credentials, I have already created a test account
!env.py file in alembic folder was altered according to app's needs