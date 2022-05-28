# groupE
This is the official repo for CSCC22B Group E.

# Prerequisites

- Python 3.10

# Installation

Create python virtual environment

> Windows: `python -m venv .venv`

Activate virtual environment

> Windows: `cd .venv/Scripts && activate && cd ../..`

Install the python libraries

> `pip install -r requirements.txt`

Create environment variables

> Windows: copy and paste `.env.example` and name it `.env`

Open and update environment variables

> DB_NAME=SCHEMA_NAME <br />
> DB_USERNAME=DATABASE_USERNAME <br />
> DB_PASSWORD=DATABASE_PASSWORD <br />

Run migrations

> `python manage.py migrate`

Run the server

> `python manage.py runserver`

Open the app at `http://localhost:8000`
