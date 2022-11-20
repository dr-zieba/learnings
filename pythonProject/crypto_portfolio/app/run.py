#/app/run.py
from app import create_app, db
import os

if __name__ == '__main__':
    flask_app = create_app()

    #create tables if not exists
    with flask_app.app_context():
        db.create_all()

    flask_app.run()