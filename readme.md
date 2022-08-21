#    How to run:

##    -1- `docker-compose up -d --build` 

##    -2- `docker exec -it <web_container_name> bash -c "./tuto.sh"` 
-> for futher instruction on how to use the App (MUST CHECK!)
-> !web_container_name is in the NAMES section of `docker ps` command when you run `docker-compse up` command

##    -3- access main page through URL: localhost:8000

##    -4- access APIs through URL: localhost:8000/docs

#    Description:
The APP will save the following attributes: post URL, post text, posting time, post image link, likes count, comments count, shares count

# Available routes:

## /scrape-page?page_name=""&page_scroll_cnt="" 
-> scrape a public page and save data to postgresql DB using public's page name and the count of how many pages to scroll through

!the bigger the "page_scroll_cnt" the more time it will take for scraping to be executed and saved in DB

## /pages 
-> view all scrapped pages' data

## /check-db 
-> check how many rows we have in the table (for checking if the API works)

# Remarks
!no need to provide credentials, I have already created a test account
!env.py file in alembic folder was altered according to app's needs