FROM python:3.8.16-alpine3.18

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt


CMD python ./main.py "https://i0.wp.com/wicks.lk/wp-content/uploads/2021/04/1604477972_778-C.jpg?fit=600%2C600&ssl=1" jpg


#[ "python","./main.py","https://i0.wp.com/wicks.lk/wp-content/uploads/2021/04/1604477972_778-C.jpg?fit=600%2C600&ssl=1","jpg"]