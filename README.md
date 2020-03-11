# Raffle Person API

A raffle random person chooser API.

## Features

With this API:
- Can list, create, update and delete raffle persons
- Can draw people.

### Requirements
```
- Python 3
- Django 3.0.4
- Django Rest Framework 3.11.0
- Postgres latest
- SWEEPSTAKE API
```

### Clone the repository
```
git clone https://github.com/marlonleite/raffle_person.git
```

### Installation

create a .env file to root dir
```
- project:
  - .env
```
update the file .env with:
```
SECRET_KEY=value
DEBUG=value
ALLOWED_HOSTS=value

DATABASE_ENGINE=value
DATABASE_USER=value
DATABASE_PASSWORD=value
DATABASE_NAME=value
DATABASE_HOST=value
DATABASE_PORT=value

SWEEPSTAKE_URL=value
```
- check the env.exemple

Virtualenv:
```
python3 --version
python3 -m venv venv
source venv/bin/activate
 
pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```

Docker:
```
Create:
docker-compose up -d

Access:
http://127.0.0.1:8000

Drop:
docker-compose down

```

## How it works:

Request URL:

List raffles:
```
GET /api/raffles/
```
```
Response 200:

[
    {
        "number": "string",
        "name": "string",
        "birthday": "string",
        "phone": "string"
    }
]
```

Create raffles:
```
POST /api/raffles/
```
```
Data json:
{
  "name": "string",
  "phone": "string",
  "birthday": "yyyy-mm-dd"
}
```
```
Response 201:
{
   "number": "string",
   "name": "string",
   "birthday": "string",
   "phone": "string"
}
```

Update raffles:
```
PATCH /api/raffles/<number>/
```
```
Data json:
{
    ...
    "name": <string>
    ...
}


```
```
Response 200:
{
   "number": "string",
   "name": "string",
   "birthday": "string",
   "phone": "string"
}
```

Delete raffles:
```
DELETE /api/employees/<number>/
```
```
Response 204 No Content
```

Raffling people:

```
GET /api/raffling/
```


```
Response 200:
{
   "number": "string",
   "name": "string",
   "birthday": "string",
   "phone": "string"
}
```

## Running the tests

Some tests were done in the application. 

Test Raffle create, list, update and delete. 
Test Person create, list, update and delete. 
Test Raffling people. 
Expected returns status of the application.

Go there:
```
./manage.py test
```

## Live Previews

* [http://raffles.marlonleite.com.br](http://raffles.marlonleite.com.br)


## Authors

* **Marlon Leite** - [GitHub](https://github.com/marlonleite)

## Links

* [Sweepstake API](https://github.com/marlonleite/sweepstake/api/)
* [Python3](https://www.python.org/download/releases/3.0/)
* [Django](https://docs.djangoproject.com)
* [Django Rest Framework](https://www.django-rest-framework.org/)

