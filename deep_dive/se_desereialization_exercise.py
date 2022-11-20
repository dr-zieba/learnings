from datetime import date, datetime
from decimal import Decimal
from json import JSONEncoder, dumps, JSONDecoder, loads

class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def to_dict(self):
        return dict(symbol=self.symbol, date=self.date, open_=self.open,
                    high=self.high, low=self.low, close=self.close, volume=self.volume)


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def to_dict(self):
        return dict(symbol=self.symbol, timestamp=self.timestamp, order=self.order,
                    price=self.price, volume=self.volume, commission=self.commission)


activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]}

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock) or isinstance(obj, Trade):
            result = obj.to_dict()
            result['object'] = obj.__class__.__name__
            return result
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            super().default(obj)

def decode_stock(d):
    s = Stock(d['symbol'],
              datetime.strptime(d['date'], '%Y-%m-%d').date(),
              Decimal(d['open_']),
              Decimal(d['high']),
              Decimal(d['low']),
              Decimal(d['close']),
              d['volume']
              )
    return s

def decode_trade(d):
    t = Trade(d['symbol'],
              datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'),
              d['order'],
              Decimal(d['price']),
              Decimal(d['commission']),
              int(d['volume'])
              )
    return t

def decode_fin(d):
    object_type = d.get('object', None)
    if object_type == 'Stock':
        return decode_stock(d)
    elif object_type == 'Trade':
        return decode_trade(d)
    else:
        return d

class CustomDecoder(JSONDecoder):
    def decode(self, arg):
        data = loads(arg)
        return self.parse_financial(data)

    def parse_financial(self, obj):
        if isinstance(obj, dict):
            obj = decode_fin(obj)
            if isinstance(obj, dict):
                for k,v in obj.items():
                    obj[k] = self.parse_financial(v)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                obj[idx] = self.parse_financial(item)
        return obj

d = {
      "symbol": "MSFT",
      "date": "2018-11-22",
      "open_": "103.25",
      "high": "103.48",
      "low": "103.07",
      "close": "103.11",
      "volume": 4493689,
      "object": "Stock"
    }

t = {
      "symbol": "AAPL",
      "timestamp": "2018-11-22T10:30:05",
      "order": "sell",
      "price": "177.01",
      "volume": 20,
      "commission": "9.99",
      "object": "Trade"
    }


encoded = dumps(activity, cls=CustomEncoder, indent=2)
# print(encoded)

decoded = loads(encoded, cls=CustomDecoder)
print(decoded)









