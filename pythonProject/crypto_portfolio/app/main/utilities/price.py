import json
import requests

def get_coin_price(symbol_id, owner_id) -> float:
    symbol = symbol_id.lower()
    base_url = "https://api.coingecko.com/api/v3"
    coin_paprika = "https://api.coinpaprika.com/v1/"

    #identifiers = None
    try:
        url2 = f"{coin_paprika}coins"
        r2 = requests.get(url2)
        a = r2.json()
        d = {coin["symbol"]: coin["id"] for coin in a if coin["id"] == "btc-bitcoin"}
        print(symbol_id)
        '''
        TODO: coin paprika api in case of coingecko limit reached.
        coinpaprika doc: https://api.coinpaprika.com/#tag/Coins/paths/~1coins/get
        TODO: maybe web scraper will be better for coin market prices ??
        Not limited to api plans.
        '''


        url = base_url + f"/simple/price?ids={symbol}&vs_currencies=usd"
        r = requests.get(url)
        data = r.json()
        print(data)
        price = data[symbol]
        val_ = [float(x) for x in price.values()]
        return round(val_[0], 2)
    except Exception as e:
        return 0

