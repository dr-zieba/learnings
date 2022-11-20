import json
from json.decoder import JSONDecodeError

from pathlib import Path

def add(symbol: str, amount: int):
    path = 'data/store.json'
    symbols = []

    with open(path, 'r+') as f:
        try:
            symbols = json.load(f)
        except:
            pass

    symbols_values = [item['symbol'] for item in symbols]

    if symbol not in symbols_values:
        data_to_append = {'symbol': symbol, 'amount': amount}
        symbols.append(data_to_append)
    else:
        print(f'Symbol {symbol} already added!')

    with open(path, 'w') as f:
        json.dump(symbols, f, indent=4)