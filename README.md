# ATM_Bank_full-stack--> A_Python_Full stack project on ATM_BANK operations.

Project Description : This is a full-stack web application for an ATM bank system developed using Django.The ATM Bank Full-Stack Application allows users to interact with an ATM-like system through a web interface. Users can verify their PIN, check their balance, make deposits and withdrawals, and change their PIN. The backend logic is handled by Django, and the frontend includes responsive design for better user experience.

## Features

- User PIN verification
- Check available balance
- Withdraw funds
- Deposit funds
- Change PIN

#### Useage

- To use the application:

- Open your web browser and navigate to http://localhost:8000/.
- You can use the admin panel at http://localhost:8000/admin/ to manage users and data.

## Endpoints

- UserInterface
GET /: Home page
POST /verify_pin/: Verify user PIN

- BankInterface
POST /available_balance/: Check available balance
POST /withdraw/: Withdraw funds
POST /deposit/: Deposit funds
POST /pin_change/: Change PIN
## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Django, python

**Database:** SQLite (default, can be changed to PostgreSQL, MySQL, etc.)

**Version Control:** Git, GitHub

## Installation

To get a local copy of the project up and running, follow these steps:

Prerequisites
- Python 3.x (3.7 & above)
- Django
- Mysql (Any SQL Enivironment Based on User's Choice)

After Python installation.
- Install Django

```bash
  pip install Django
```

- Install Mysql-connector

```bash
  pip install mysql-connector-python
```

- Start django your first project 

```bash
  django-admin startproject projectname
```


- Create your first app & Run development server

  ```bash
  django-admin startapp appname
  
  #After completeion of app
  python manage.py runserver
```


