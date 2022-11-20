from flask_sqlalchemy import SQLAlchemy
from price import check
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Coin(db.Model):
    __tablename__ = "coins"

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(12), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    def __int__(self, symbol, amount, owner_id):
        self.symbol = symbol
        self.amount = amount
        self.owner_id = owner_id

    def call_values(self):
        return check(self.symbol)

    def call_price(self):
        price = check(self.symbol)
        return float(price) * float(self.amount)


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=False)
    password = db.Column(db.String(200), nullable=False, unique=False, primary_key=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def __init__(self, name):
        self.name = name
        self.created_on = datetime.now()
        self.last_login = datetime.now()

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

