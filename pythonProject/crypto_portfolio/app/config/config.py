#/app/config/config.py

#To connect with CLI to DB
#use:
#psql -U user_name  -h 127.0.0.1 -d db_name

import os

#Postgres configuration
db_host = os.environ.get('DB_HOST', default='0.0.0.0')
db_name = os.environ.get('DB_NAME', default='crypto')
db_password = os.environ.get('DB_PASSWORD', default='crypto')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USERNAME', default='crypto')

SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#Flask configuration
SECRET_KEY="secret"
DEBUG=True
