# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./src /app

#
RUN sed -i -e 's/\r$//' ./tuto.sh

#
RUN sed -i -e 's/\r$//' ./check.sh

#
RUN sed -i -e 's/\r$//' ./scrape.sh

#CMD command is in the compose file!



