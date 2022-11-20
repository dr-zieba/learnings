#/app/main/__init__.py

from flask import Blueprint

#create blueprint for routes
main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

#import at bottom to avoid import conflict in /app/main/routes.py
from app.main import routes
