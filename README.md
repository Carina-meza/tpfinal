# TP Final informatorio

## Create Virtual Environment
python -m venv .env

## Load Virtual Environment (deactivate to leave virtual env)
source .env/Scripts/activate

## Install requirements
pip install django==3.0
pip install django-mssql-backend
pip install pillow

## Migrate DB (install mssql server and create DB TPFINAL)
py manage.py migrate

## Create database scripts from python code
py manage.py makemigrations

## Create super user
py manage.py createsuperuser 

## Run server
py manage.py runserver
