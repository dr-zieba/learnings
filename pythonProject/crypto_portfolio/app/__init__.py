#/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.login'
login_manager.session_protection = 'strong'

def create_app():
    app = Flask(__name__, static_folder='main/static')
    cfg = os.path.join(os.getcwd(), 'config', 'config.py')
    app.config.from_pyfile(cfg)

    #init db models
    #db.create_all()
    db.init_app(app)
    #init bootstrap
    bootstrap.init_app(app)
    #init login_manager
    login_manager.init_app(app)

    #import blueprint from /app/main/__init__.py
    from app.main import main
    app.register_blueprint(main)

    #import blueprint from /app/auth/__init__.py
    from app.auth import authentication
    app.register_blueprint(authentication)

    return app


