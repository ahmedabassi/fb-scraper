#!/bin/sh

echo Enter page name: 
read pageName 
echo Enter page count:
read pageCnt 

#dnt forget shell script variables syntax "a=b mich a = b :)"
URL="http://localhost:8000/scrape-page/?page_name="
URL="${URL}${pageName}&page_scroll_cnt=${pageCnt}"

curl -X 'POST' "${URL}" -H 'accept: application/json' -d ''



