from flask import Flask, render_template, request, flash, redirect, url_for
from display import display
from models import Coin, db, User
from price import check
from flask_login import LoginManager
from forms import SignupForm, LoginForm
from flask_login import login_required, logout_user, login_user, current_user
from views import views
from sqlalchemy.sql import func
from views import login_manager

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="secret")
app.register_blueprint(views)

test_config = None
if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
else:
    app.config.from_mapping(test_config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.jinja_env.globals.update(check=check)

login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
