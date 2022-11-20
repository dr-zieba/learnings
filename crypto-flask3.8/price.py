import json
import requests

def check(symbol = 'btc') -> float:
    symbol = symbol.lower()
    #identifiers = None
    try:
        base_url = "https://api.coingecko.com/api/v3"
        url = base_url + "/coins/list"
        r = requests.get(url)
        identifiers = r.json()
        symbol_id_map = {d["symbol"]: d["id"] for d in identifiers}
    except:
        return 0

    try:
        url = base_url + f"/simple/price?ids={symbol_id_map[symbol]}&vs_currencies=usd"
        r = requests.get(url)
        data = r.json()
        price = data[symbol_id_map[symbol]]
        val_ = [float(x) for x in price.values()]
        return round(val_[0], 2)
    except:
        return 0

