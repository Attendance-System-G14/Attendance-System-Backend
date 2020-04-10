# pull official base image
FROM python:3.8.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# set work directory
RUN mkdir /code
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install gunicorn

# copy project
COPY . /code/

# run entrypoint.prod.sh
ENTRYPOINT ["/code/entrypoint.sh"]