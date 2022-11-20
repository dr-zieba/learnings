import tkinter as tk
from interfaces.syling import *
from interfaces.logging_component import Logging
from binance_future_api import BinanceFutureConnector
from interfaces.watchlist_component import Watchlist
from interfaces.trades_component import TradesWatch
from interfaces.strategy_component import StrategyEditor
import logging
import time

logger = logging.getLogger()

class Root(tk.Tk):
    def __init__(self, binance: BinanceFutureConnector):
        super().__init__()

        self.binance = binance

        self.title("Trading bot")
        self.configure(bg=BG_COLOR)
        #self.geometry("1024x768")

        self._left_frame = tk.Frame(self, bg=BG_COLOR)
        self._left_frame.pack(side=tk.LEFT)

        self._right_frame = tk.Frame(self, bg=BG_COLOR)
        self._right_frame.pack(side=tk.LEFT)

        self._watchlist_frame = Watchlist(self.binance.contracts, self._left_frame, bg=BG_COLOR)
        self._watchlist_frame.pack(side=tk.TOP)

        self.logging_frame = Logging(self._left_frame, bg=BG_COLOR)
        self.logging_frame.pack(side=tk.TOP)

        self._strategy_frame = StrategyEditor(self, self.binance, self._right_frame, bg=BG_COLOR)
        self._strategy_frame.pack(side=tk.TOP)

        self._trades_frame = TradesWatch(self._right_frame, bg=BG_COLOR)
        self._trades_frame.pack(side=tk.TOP)

        self._update_ui()

    def _update_ui(self):
        #func checks log list for not displayed logs and call add_log with msg from log file
        for log in self.binance.logs:
            if not log['displayed']:
                self.logging_frame.add_log(log['log'])
                log['dispayed'] = True

        try:
            for key, value in self._watchlist_frame.body_widget['symbol'].items():
                symbol = self._watchlist_frame.body_widget['symbol'][key].cget('text')

                if symbol not in self.binance.contracts:
                    continue

                if symbol not in self.binance._prices:
                    self.binance.get_bid_ask(self.binance.contracts[symbol])
                    continue

                prices = self.binance._prices[symbol]

                if prices['bid'] is not None:
                    self._watchlist_frame.body_widget['bid_var'][key].set(prices['bid'])

                if prices['ask'] is not None:
                    self._watchlist_frame.body_widget['ask_var'][key].set(prices['ask'])
        except RuntimeError as e:
            logger.error(f"Error while looping thrue watch list dictionary:{e}")


        #after call again func to check and add new logs
        self.after(1500, self._update_ui)
