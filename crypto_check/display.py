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
    print("Your crypto:")
    for item in symbols:
        _, price = check(item['symbol'])
        my_value = price * float(item['amount'])
        print(f"Symbol: {item['symbol']} Amount: {item['amount']} Value: {price}$ My values: {my_value}$")
        total += my_value
    print(f"Total value of your crypto: {total}$")
