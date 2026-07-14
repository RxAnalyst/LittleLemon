# LittleLemon
This is backened developer capston project
## Project Description
This is the Capstone Project for the Meta Back-End Developer Certificate.
It is a REST API for the Little Lemon restaurant built using Django and Django REST Framework.

## Features
- User registration and authentication
- Token authentication using Djoser
- Restaurant menu management
- Table booking API
- Admin panel
- API endpoints

## Technologies Used
- Python
- Django
- Django REST Framework
- Djoser
- mysql

## Installation

Clone the repository

```bash
https://github.com/RxAnalyst/LittleLemon.git

Go into the project

```bash
cd LittleLemon
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```
change directory
cd littlelemon

Install dependencies

```bash
pip install -r requirements.txt
```


Apply migrations

```bash
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /auth/users/ | POST | Register user |
| /auth/token/login/ | POST | Login |
| /restaurant/menu/ | GET | View menu |
| /restaurant/menu/ | POST | Add menu item |
| /restaurant/booking/table | GET | View bookings |


## Running Tests

```bash
python manage.py test
```

## Admin

Create an admin account

```bash
python manage.py createsuperuser
```

Then visit

```
http://127.0.0.1:8000/admin/
```

## Author

RxAnalyst