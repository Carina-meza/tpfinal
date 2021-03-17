# TP Final informatorio

## Create Virtual Environment
pip install virtualenv
virtualenv .env
### OR
python -m venv .env

## Load Virtual Environment (bash)
source .env/Scripts/activate
### OR (cmd)
.env\Scripts\activate
## "deactivate" to leave virtual env

## Install requirements
pip install django==3.0
pip install django-mssql-backend
pip install pillow
pip install django-extensions

## Migrate DB (install mssql server and create DB TPFINAL)
py manage.py migrate

## Create database scripts from python code
py manage.py makemigrations

## Create super user
py manage.py createsuperuser 

## Run server
py manage.py runserver
