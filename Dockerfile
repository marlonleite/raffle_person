# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /code/

COPY docker-entrypoint.sh /code/
WORKDIR /code/

# expose the port 8000
EXPOSE 8000

ENTRYPOINT ["sh", "docker-entrypoint.sh"]