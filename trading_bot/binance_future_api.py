import time
import requests
import logging
import hmac
import hashlib
from urllib.parse import urlencode

#pip install websocket-client===0.57.0
#with different version wss do not work!!!!
import websocket
import json
import threading
import typing

from strat import TechnicalStrategy, BrakeoutStrategy

from models import *


#API Key = 483cff47fbf4215944fd7b69e2f7c05474d521522a5b889cf9b90e707cd0de3a
#API Secret = d4e4306bd1076eca458f35a4b195ae7bbfba0a39b3671bdd6de8e43c7848c05b

logger = logging.getLogger()

class BinanceFutureConnector(object):
    #class initiate connection towards binance future testnet
    #class build of base url, dictionary of prices
    def __init__(self, api_key: str, api_secret: str):
        self._base_url = 'https://testnet.binancefuture.com'
        self._wss_url = "wss://stream.binancefuture.com/ws"
        self._prices = dict()
        self._api_key = api_key
        self._api_secret = api_secret
        self._headers = {'X-MBX-APIKEY': self._api_key}

        #at init call get_contracts to store available contracts/pairs to trade
        self.contracts = self.get_contract()

        #at init call get_balances to store available balance
        self.balances = self.get_account_balance()

        #Initialization of w web socket
        #needs to be initialized to use send method
        self._ws = None
        #ID of subscribed channel to wss binance
        #ID must be unique in request and gets incremented with every methode call
        self._ws_id = 1

        #init list for logs from web socket
        self.logs = []

        self.strategies: typing.Dict[int, typing.Union[TechnicalStrategy, BrakeoutStrategy]] = dict()

        #wss must run in separate thread to allow rest of code to be executed. Otherwise progrm will be blocked on start_web_socket()
        t = threading.Thread(target=self._start_web_socket)
        t.start()

        logger.info("Initialized connection towards binance future")

    def _add_log(self, msg):
        #func add logs to logs list with 'display' flag
        #logger.info(msg)
        self.logs.append({"log": msg, "displayed": False})

    def _generate_signature(self, data: typing.Dict) -> str:
        return hmac.new(self._api_secret.encode(), urlencode(data).encode(), hashlib.sha256).hexdigest()

    def _make_requeste(self, method: str, endpoint: str, data: typing.Dict):
        #methode to create requests
        #base methode for building requestes
        if method == 'GET':
            try:
                response = requests.get(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error(f"Error on method {method}: {e}")
                return None
        elif method == 'POST':
            try:
                response = requests.post(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error(f"Error on method {method}: {e}")
                return None
        elif method == 'DELETE':
            try:
                response = requests.delete(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error(f"Error on method {method}: {e}")
                return None
        else:
            raise ValueError()

        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f'{response.status_code} {self._base_url}{endpoint} {method} {response.json()}')
            return None

    def get_contract(self) -> typing.Dict[str, Contract]:
        #methode to call binance with all available trading pairs
        #pairs returned as dict with relavent data
        exchange_info = self._make_requeste('GET', '/fapi/v1/exchangeInfo', dict())

        contracts = dict()

        #contract not NONE if make_requests() returned something
        if exchange_info is not None:
            for item in exchange_info['symbols']:
                contracts[item['symbol']] = Contract(item)

        return contracts

    def get_bid_ask(self, contract: Contract) -> typing.Dict[str, float]:
        #methode calls binance future to returen bid and ask prices for particular pairs eq. BTCUSDT
        data = dict()
        data['symbol'] = contract.symbol
        obj_data = self._make_requeste('GET', '/fapi/v1/ticker/bookTicker', data)

        if obj_data is not None:
            if contract.symbol not in self._prices:
                self._prices[contract.symbol] = {'bid': float(obj_data['bidPrice']), 'ask': float(obj_data['askPrice'])}
            else:
                self._prices[contract.symbol]['bid'] = float(obj_data['bidPrice'])
                self._prices[contract.symbol]['askPrice'] = float(obj_data['askPrice'])

            return self._prices[contract.symbol]

    def get_historical_candles(self, contract: Contract, interval: str) -> typing.List[Candel]:
        data = dict()
        data['symbol'] = contract.symbol
        data['interval'] = interval
        data['limit'] = 1000

        response = self._make_requeste("GET", "/fapi/v1/klines", data)

        candles = []

        #c[0] = open time, c[1] = open price, c[2] = hight price, c[3] = low price, c[4] = close price, c[5] = volume
        if response is not None:
            for c in response:
                candles.append(Candel(c))

        #candles list contains list of candles in called interval time
        #-1 is last candel
        #print(candles[-1].open)

        return candles

    def get_account_balance(self) -> typing.Dict[str, Balance]:
        data = dict()
        data['timestamp'] = int(time.time() * 1000)
        data['signature'] = self._generate_signature(data)

        balance = dict()

        response = self._make_requeste("GET", "/fapi/v1/account", data)

        if response is not None:
            for asset in response['assets']:
                balance[asset['asset']] = Balance(asset)

        #with models class Balance wallet assets can be returned as:
        #print(balance['USDT'].wallet_balance)

        return balance

    def get_order_status(self, contract: Contract, orderid: int) -> OrderStatus:
        data = dict()
        data['timestamp'] = int(time.time() * 1000)
        data['symbol'] = contract.symbol
        data['orderId'] = orderid
        data['signature'] = self._generate_signature(data)

        response = self._make_requeste("GET", "/fapi/v1/order", data)

        if response is not None:
            response = OrderStatus(response)

            return response

    def place_order(self, contract: Contract, side: str, quantity: float, order_type: str, price=None, tif=None) -> OrderStatus:
        #eq params:
        #symbol: crypto to buy
        #side: buy/sell
        #tif: timeInForce
        data = dict()
        data['symbol'] = contract.symbol
        data['side'] = side
        data['quantity'] = quantity
        data['type'] = order_type

        if price is not None:
            data['price'] = price
        if tif is not None:
            data['timeInForce'] = tif

        data['timestamp'] = int(time.time() * 1000)
        data['signature'] = self._generate_signature(data)

        response = self._make_requeste("POST", "/fapi/v1/order", data)

        if response is not None:
            response = OrderStatus(response)

        return response

    def cancel_order(self, contract: Contract, orderid: int) -> OrderStatus:
        data = dict()
        data['symbol'] = contract.symbol
        data['orderId'] = orderid
        data['timestamp'] = int(time.time() * 1000)
        data['signature'] = self._generate_signature(data)

        response = self._make_requeste("DELETE", "/fapi/v1/order", data)

        if response is not None:
            response = OrderStatus(response)

        return response

    def _start_web_socket(self):
        self.ws = websocket.WebSocketApp(self._wss_url, on_open=self._on_open, on_close=self._on_close, on_error=self._on_error,
                                    on_message=self._on_message)

        #connection in while infinit loop in case of drop of connection and automatic reconnection with 2sec wait
        while True:
            try:
                self.ws.run_forever()
            except Exception as e:
                logger.error(f"Error with web socket connection: {e}")
            time.sleep(2)

    def _on_open(self):
        logger.info("Binance wss connection opened")
        print(self.contracts.values())
        self.subscribe_channel(list(self.contracts.values()), "bookTicker")

    def _on_close(self):
        logger.warning("Binance wss connection closed")

    def _on_error(self, msg: str):
        logger.error(f"Binance wss error: {msg}")

    def _on_message(self, msg: str):
        data = json.loads(msg)

        #ask price represents the minimum price that a seller is willing to take for that same security.
        #bid price is a price for which somebody is willing to buy

        if "e" in data:
            if data['e'] == "bookTicker":
                symbol = data['s']
                if symbol not in self._prices:
                    self._prices[symbol] = {'bid': float(data['b']), 'ask': float(data['a'])}
                else:
                    self._prices[symbol]['bid'] = float(data['b'])
                    self._prices[symbol]['ask'] = float(data['a'])
                #print(self._prices)

            elif data['e'] == "aggTrade":
                symbol = data['s']

                for key, start in self.strategies.items():
                    if start.contract.symbol == symbol:
                        start.parse_trade(float(data['p']), float(data['q']), data['T'])

                '''
                #add logs to log list
                if symbol == "BTCUSDT":
                    self._add_log(f"{symbol} {str(self._prices[symbol]['bid'])} / {str(self._prices[symbol]['ask'])}")
                '''

    def subscribe_channel(self, contracts: typing.List[Contract], channel: str):
        data = dict()
        data['method'] = "SUBSCRIBE"
        data['params'] = []

        for contract in contracts:
            data['params'].append(contract.symbol.lower() + "@" + channel)
        data['id'] = self._ws_id

        #Binance requires json data type in request
        try:
            self.ws.send(json.dumps(data))
        except Exception as e:
            logger.error(f"Error during subscription do channel {data['params']}: {e}")

        self._ws_id += 1

