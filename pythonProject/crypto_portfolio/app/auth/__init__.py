#/app/auth/__init__.py

from flask import Blueprint

#create blueprint for routes
authentication = Blueprint('authentication', __name__, template_folder='templates', static_folder='static')

#import at bottom to avoid import conflict in /app/main/routes.py
from app.auth import routes

