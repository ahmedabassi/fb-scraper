#    How to run:

##    -1- `docker-compose up -d --build` 

##    -2- `docker exec -it <web_container_name> bash -c "./tuto.sh"` 
-> for futher instruction on how to use the App (MUST CHECK!)
-> ! web_container_name is in the NAMES section of `docker ps` command when you run `docker-compse up` command

##    -3- access main page through URL: localhost:8000

##    -4- access APIs through URL: localhost:8000/docs

#    Description:
The APP will save the following attributes: post URL, post text, posting time, post image link, likes count, comments count, shares count

# Available routes:

## /scrape-page?page_name=""&page_scroll_cnt="" 
-> scrape a public page and save data to postgresql DB using public's page name and the count of how many pages to scroll through (I recommend you use 2 pages)

!the bigger the "page_scroll_cnt" the more time it will take for scraping to be executed and saved in DB

## /pages 
-> view all scrapped pages' data

## /check-db 
-> check how many rows we have in the table (for checking if the API works)

# How to access the DataBase
1. Run the following command: `docker exec -it <db_container_name> bash`
2. Connect postgres DB psql using: `psql -U postgres`
3. Change to fb DB via : `\c fb`
4. View data via: `select * from "FBPAGE";`
5. exit via: CTRL+Z

! FBPAGE is the only table present in this APP and all data are saved into it

# Remarks
no need to provide credentials, I have already created a test account

env.py file in alembic folder was altered according to app's needs