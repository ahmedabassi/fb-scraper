#!/bin/bash

echo "###########################################################################################################"
frst="Welcome to Ahmed's test app"
echo ${frst}

echo ""

started="To get started use the following command ---> docker exec -it <web_container_name> bash -c ./scrape.sh"
echo ${started}

pg="    - page_name : page name from Facebook's public page url (e.g https://www.facebook.com/<page_name>)"
av="    - page_cnt : how many pages to view when scraping, the more pages you use the longer the program will take"
echo Input variables are the following: ; echo ${pg} ; echo ${av}

echo ""

check="To check if it worked use the following command ---> docker exec -it <web_container_name> bash -c ./check.sh"
echo ${check}

echo ""

bye="I hope to hear from you soon!"
echo  ${bye}
echo "###########################################################################################################"



