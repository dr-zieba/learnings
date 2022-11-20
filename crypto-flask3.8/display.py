import json
from price import check

def display():
    path = 'data/store.json'
    symbols = []

    with open(path, 'r') as f:
        try:
            symbols = json.load(f)
        except:
            pass

    total = 0
    coins = []
    print("Your crypto:")
    for item in symbols:
        _, price = check(item['symbol'])
        my_value = price * float(item['amount'])
        coins.append((item['symbol'], item['amount'], price, my_value))

    return coins