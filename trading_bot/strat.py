import logging
from models import *
from typing import *
import pandas as pd

logger = logging.getLogger()

TS_EQUIV = {"1m": 60, "5m": 300, "15m": 900, "30m": 1800, "1h": 3600, "4h": 14400}

class Strategy:
    def __init__(self, contract: Contract, timeframe: str, balance_pct: float, take_profit: float, stop_loss: float):
        self.contract = contract
        self.timeframe = timeframe
        self.ts_equiv = TS_EQUIV[timeframe] * 1000
        self.balance_pct = balance_pct
        self.take_profit = take_profit
        self.stop_loss = stop_loss

        self.candles: typing.List[Candel] = []

    def parse_trade(self, price: float, size: float, timestamp: int) -> str:

        last_candle = self.candles[-1]

        # same candle
        if timestamp < last_candle.timestamp + self.ts_equiv:
            last_candle.close = price
            last_candle.volume += size
            if price > last_candle.high:
                last_candle.high = price
            elif price < last_candle.low:
                last_candle.low = price

            return "same_candle"

        # missing candle
        elif timestamp >= last_candle.timestamp + 2 * self.ts_equiv:

            missing_candles = int((timestamp - last_candle.timestamp) / self.ts_equiv) -1

            logger.info(f"Missing {missing_candles} for {self.contract.symbol}, {self.timeframe}")

            for missing in range(missing_candles):
                new_ts = last_candle.timestamp + self.ts_equiv
                candle_info = [new_ts, last_candle.close, last_candle.close, last_candle.close, last_candle.close, 0]

                new_candle = Candel(candle_info)

                self.candles.append(new_candle)

                last_candle = new_candle

            new_ts = last_candle.timestamp + self.ts_equiv
            candle_info = [new_ts, price, price, price, price, size]
            new_candle = Candel(candle_info)

            self.candles.append(new_candle)

            return "new_candle"

        # new candle
        elif timestamp >= last_candle.timestamp + self.ts_equiv:
            new_ts = last_candle.timestamp + self.ts_equiv
            candle_info = [new_ts, price, price, price, price, size]
            new_candle = Candel(candle_info)

            self.candles.append(new_candle)

            logger.info(f"New candle for {self.contract.symbol}, {self.timeframe}")

            return "new_candle"


class TechnicalStrategy(Strategy):
    def __init__(self, contract: Contract, timeframe: str, balance_pct: float, take_profit: float, stop_loss: float, other_params: typing.Dict):
        super().__init__(contract, timeframe, balance_pct, take_profit, stop_loss)

        self._ema_fast = other_params['ema_fast']
        self._ema_slow = other_params['ema_slow']
        self._ema_signal = other_params['ema_signal']

    def _rsi(self):
        return

    def _macd(self) -> Tuple[float, float]:
        close_list = []
        for candle in self.candles:
            close_list.append(candle.close)

        closes = pd.Series(close_list)

        ema_fast = closes.ewm(span=self._ema_fast).mean()
        ema_slow = closes.ewm(span=self._ema_slow).mean()

        macd_line = ema_fast - ema_slow
        macd_signal = macd_line.ewm(span=self._ema_signal).mean()

        return macd_line[-2], macd_signal[-2]

    def _check_signal(self):
        macd_line, macd_signal = self._macd()



class BrakeoutStrategy(Strategy):
    def __init__(self, contract: Contract, timeframe: str, balance_pct: float, take_profit: float, stop_loss: float, other_params: typing.Dict):
        super().__init__(contract, timeframe, balance_pct, take_profit, stop_loss)

        self._min_volume = other_params['min_volume']

    def check_signal(self) -> int:
        if self.candles[-1].close > self.candles[-2].high and self.candles[-1].volume > self._min_volume:
            return 1
        elif self.candles[-1].close < self.candles[-2].low and self.candles[-1].volume > self._min_volume:
            return -1
        else:
            return 0