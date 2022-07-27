FROM python:3.8.13-buster
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN echo 'hola'
RUN pip install --no-cache-dir -r requirements.txt
RUN ls /usr/src/app
CMD ["python","./mongo.py"]

