import logging

#innit of a logger
from binance_future_api import BinanceFutureConnector

from interfaces.root_component import Root

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#set logger for console output
stream_handler = logging.StreamHandler()
formater = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formater)
stream_handler.setLevel(logging.INFO)

#set logger for file output
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formater)
file_handler.setLevel(logging.INFO)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFutureConnector('483cff47fbf4215944fd7b69e2f7c05474d521522a5b889cf9b90e707cd0de3a',
                                 'd4e4306bd1076eca458f35a4b195ae7bbfba0a39b3671bdd6de8e43c7848c05b')
    #cont = bfc.get_contract()
    #print(cont)
    #print(bfc.get_bid_ask(cont["ETHUSDT"]))
    #print(bfc.get_historical_candles(cont["BTCUSDT"], '1h')[-1].close)
    #b = bfc.get_account_balance()
    #print(b["USDT"].wallet_balance)

    root = Root(binance)
    root.mainloop()