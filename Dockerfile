FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /source
WORKDIR /source
COPY requirements.txt /source/
RUN apt update
RUN apt install -y gcc libpq-dev python3-dev
RUN pip3 install -r /source/requirements.txt
COPY source /source/

WORKDIR /source

ENV FLASK_APP main.py

EXPOSE 5000

CMD flask run -h 0.0.0.0 -p 5000