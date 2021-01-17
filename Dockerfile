FROM python:3.7

ENV PYTHONNUMBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/