from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'TPFINAL',
        'Trusted_Connection': 'yes',
        'HOST': 'localhost\\SQLEXPRESS',
        'OPTIONS': {
            'driver':'SQL Server Native Client 11.0'
        }
    }
}
