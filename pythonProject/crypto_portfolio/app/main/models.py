from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.main.utilities import get_coin_price
import requests
from flask_login import current_user
from sqlalchemy.ext.hybrid import hybrid_property


class Coin(db.Model):
    __tablename__ = "coins"

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(12), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    symbol_id = db.Column(db.String(36), nullable=False)

    def __repr__(self):
        return f'[{self.symbol},{self.amount},{self.owner_id},{self.symbol_id}]'

    def __getitem__(self, item):
        lst = [self.symbol, self.amount, self.owner_id, self.symbol_id]
        return lst[item]

    @classmethod
    def coin_identifier(cls, symbol):
        try:
            base_url = "https://api.coingecko.com/api/v3"
            url = base_url + "/coins/list"
            r = requests.get(url)
            identifiers = r.json()
            symbol_id_map = {d["symbol"]: d["id"] for d in identifiers}
            print(symbol_id_map[symbol])
            return symbol_id_map[symbol]
        except:
            return identifiers['status']['error_code']

    def call_price(self):
        price = get_coin_price(self.symbol_id, self.owner_id)
        total_value = float(price) * float(self.amount)
        return price, total_value
