# tpfinal
TP Final informatorio

#Load Virtual Environment
source venv/Scripts/activate

#install requirements
pip install django==3.0
pip install django-mssql-backend

#migrate DB (install mssql server and create DB TPFINAL)
py manage.py migrate

#create database scripts from python code
py manage.py makemigrations

#run server
py manage.py runserver
