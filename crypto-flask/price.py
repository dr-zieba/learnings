import json
import requests

def check(symbol: str) -> str:
    symbol = symbol.lower()
    try:
        base_url = "https://api.coingecko.com/api/v3"
        url = base_url + "/coins/list"
        r = requests.get(url)
        identifiers = r.json()
    except Exception as e:
        print(f"Error: {e}")

    symbol_id_map = {d["symbol"]: d["id"] for d in identifiers}

    try:
        url = base_url + f"/simple/price?ids={symbol_id_map[symbol]}&vs_currencies=usd"
        r = requests.get(url)
        data = r.json()
        price = data[symbol_id_map[symbol]].values()
        name = f"{symbol_id_map[symbol]}"
        return name, *price
    except Exception as e:
        print(f"Error: {e}")

