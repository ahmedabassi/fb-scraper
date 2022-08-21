#!/bin/bash

echo "###########################################################################################################"
frst="Welcome to Ahmed's test app"
echo ${frst}

echo ""

echo "Please note that <web_container_name> is in the NAMES section of \"docker ps\" command when you run the \"docker-compse up\" command"
scrape="./scrape.sh"
started="To get started use the following command ---> docker exec -it <web_container_name> bash -c \"${scrape}\""
echo ${started}

pg="    - page_name : page name from Facebook's public page url (e.g https://www.facebook.com/<page_name>)"
av="    - page_cnt : how many pages to view when scraping, the more pages you use the longer the program will take( I recommend you use 2 pages)"
echo Input variables are the following: ; echo ${pg} ; echo ${av}

echo ""

c="./check.sh"
check="To check if it worked use the following command ---> docker exec -it <web_container_name> bash -c \"${c}\""
echo ${check}

echo ""

f="If you want to see what has been scrapped, I suggest you use FastApi's SwaggerUI with the /pages API"
echo ${f}

bye="I hope to hear from you soon!"
echo  ${bye}
echo "###########################################################################################################"



