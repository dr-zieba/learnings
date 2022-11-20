import tkinter as tk
import typing

from interfaces.syling import *
from binance_future_api import BinanceFutureConnector
from strat import TechnicalStrategy, BrakeoutStrategy

class StrategyEditor(tk.Frame):
    def __init__(self, root, binance: BinanceFutureConnector, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.root = root
        self._all_contracts = []
        self._all_timeframes = ["1m", "5m", "15m", "30m", "1h", "4h"]

        self.binance = binance

        for symbol, contract in binance.contracts.items():
            self._all_contracts.append(symbol)

        self._commands_frame = tk.Frame(self, bg=BG_COLOR)
        self._commands_frame.pack(side=tk.TOP)

        self._table_frame = tk.Frame(self, bg=BG_COLOR)
        self._table_frame.pack(side=tk.TOP)

        self._add_button = tk.Button(self._commands_frame, text="Add strategy", font=GLOBAL_FONT, command=self._add_strategy_row, bg=BG_COLOR2, fg=FG_COLOR)
        self._add_button.pack(side=tk.TOP)

        self._headers = ["Strategy", "Contract", "TimeFrame", "Balance %", "TP %", "SL %"]

        #stores params from pop up parameter window
        self._additional_parameters = dict()

        self._extra_input = dict()

        self._base_params = [
            {"code_name": "strategy_type", "widget": tk.OptionMenu, "data_type": str, "values": ["Technical", "Brakeout"], "width": 10},
            {"code_name": "contract", "widget": tk.OptionMenu, "data_type": str, "values": self._all_contracts, "width": 15},
            {"code_name": "timeframe", "widget": tk.OptionMenu, "data_type": str, "values": self._all_timeframes, "width": 10},
            {"code_name": "balance_pct", "widget": tk.Entry, "data_type": float, "width": 10},
            {"code_name": "take_profit", "widget": tk.Entry, "data_type": float, "width": 10},
            {"code_name": "stop_loss", "widget": tk.Entry, "data_type": float, "width": 10},
            {"code_name": "parameters", "widget": tk.Button, "data_type": float, "width": 10, "text": "Parameters", "bg": BG_COLOR2, "command": self._show_popup},
            {"code_name": "activation", "widget": tk.Button, "data_type": float, "width": 10, "text": "OFF", "bg": "darkred", "command": self._switch_startagy},
            {"code_name": "delete", "widget": tk.Button, "data_type": float, "width": 10, "text": "X", "bg": "darkred", "command": self._delete_row},
        ]

        self._extra_parameters = {
            "Technical": [
                {"code_name": "ema_fast", "name": "MACD Fast Length", "widget": tk.Entry, "data_type": int},
                {"code_name": "ema_slow", "name": "MACD Slow Length", "widget": tk.Entry, "data_type": int},
                {"code_name": "ema_signal", "name": "MACD Signal Length", "widget": tk.Entry, "data_type": int}
            ],
            "Brakeout": [
                {"code_name": "min_volume", "name": "Minimum Volume", "widget": tk.Entry, "data_type": float}
            ]
        }

        self.body_widget = dict()

        for idx, h in enumerate(self._headers):
            header = tk.Label(self._table_frame, text=h, bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
            header.grid(row=0, column=idx)

        for h in self._base_params:
            self.body_widget[h['code_name']] = dict()
            if h['widget'] == tk.OptionMenu:
                self.body_widget[h['code_name'] + "_var"] = dict()

        self._body_index = 1

    def _add_strategy_row(self):
        b_index = self._body_index

        for col, base_param in enumerate(self._base_params):
            code_name = base_param['code_name']
            if base_param['widget'] == tk.OptionMenu:
                self.body_widget[code_name + "_var"][b_index] = tk.StringVar()
                self.body_widget[code_name + "_var"][b_index].set(base_param['values'][0])
                self.body_widget[code_name][b_index] = tk.OptionMenu(self._table_frame,
                                                                     self.body_widget[code_name + "_var"][b_index],
                                                                     *base_param['values'])
                self.body_widget[code_name][b_index].config(width=base_param['width'])

            elif base_param['widget'] == tk.Entry:
                self.body_widget[code_name][b_index] = tk.Entry(self._table_frame, justify=tk.CENTER)
            elif base_param['widget'] == tk.Button:
                self.body_widget[code_name][b_index] = tk.Button(self._table_frame, text=base_param['text'],
                                                                 bg=base_param['bg'], fg=FG_COLOR,
                                                                 command=lambda command=base_param['command']: command(b_index))
            else:
                continue

            self.body_widget[code_name][b_index].grid(row=b_index, column=col)

        self._additional_parameters[b_index] = dict()

        for strat, params in self._extra_parameters.items():
            for param in params:
                #by default params in popup window are blank == None
                self._additional_parameters[b_index][param['code_name']] = None


        self._body_index += 1

    def _show_popup(self, b_index: int):

        x = self.body_widget["parameters"][b_index].winfo_rootx()
        y = self.body_widget["parameters"][b_index].winfo_rooty()
        self._popup_window = tk.Toplevel(self)
        self._popup_window.wm_title("Parameters")
        self._popup_window.config(bg=BG_COLOR)
        #-topmost - pops windows over main window
        self._popup_window.attributes("-topmost", "true")
        #blocks main window, clicable will be only popup
        self._popup_window.grab_set()
        #sets popup window location under parameter button
        self._popup_window.geometry(f"+{x - 50}+{y + 30}")

        strategy_selected = self.body_widget['strategy_type_var'][b_index].get()

        row_nb = 0

        for param in self._extra_parameters[strategy_selected]:
            code_name = param['code_name']

            temp_label = tk.Label(self._popup_window, bg=BG_COLOR, fg=FG_COLOR, text=param['name'], font=BOLD_FONT)
            temp_label.grid(row=row_nb, column=0)

            if param['widget'] == tk.Entry:
                self._extra_input[code_name] = tk.Entry(self._popup_window, bg=BG_COLOR2, justify=tk.CENTER, fg=FG_COLOR, insertbackground=FG_COLOR)
                if self._additional_parameters[b_index][code_name] is not None:
                    self._extra_input[code_name].insert(tk.END, str(self._additional_parameters[b_index][code_name]))
            else:
                continue

            self._extra_input[code_name].grid(row=row_nb, column=1)

            row_nb += 1

        #validation button
        validation_button = tk.Button(self._popup_window, text="Validate", bg=BG_COLOR2, fg=FG_COLOR,
                                      command=lambda: self._validate_parameters(b_index))
        validation_button.grid(row=row_nb, column=0, columnspan=2)

    def _validate_parameters(self, b_index: int):
        strategy_selected = self.body_widget['strategy_type_var'][b_index].get()
        for param in self._extra_parameters[strategy_selected]:
            code_name = param['code_name']

            #check if any parameters are already stored
            if self._extra_input[code_name].get() == "":
                self._additional_parameters[b_index][code_name] = None
            else:
                self._additional_parameters[b_index][code_name] = param['data_type'](self._extra_input[code_name].get())


        self._popup_window.destroy()

    def _switch_startagy(self, b_index: int):

        for param in ["balance_pct", "take_profit", "stop_loss"]:
            if self.body_widget[param][b_index].get() == "":
                self.root.logging_frame.add_log(f"Missing {param} parameter")
                return

        strategy_selected = self.body_widget['strategy_type_var'][b_index].get()

        for param in self._extra_parameters[strategy_selected]:
            if self._additional_parameters[b_index][param['code_name']] is None:
                self.root.logging_frame.add_log(f"Missing {param['code_name']} parameter")
                return

        symbol = self.body_widget['contract_var'][b_index].get()
        timeframe = self.body_widget['timeframe_var'][b_index].get()
        contract = self.binance.contracts[symbol]
        balance_pct = float(self.body_widget['balance_pct'][b_index].get())
        take_profit = float(self.body_widget['take_profit'][b_index].get())
        stop_loss = float(self.body_widget['stop_loss'][b_index].get())

        if self.body_widget['activation'][b_index].cget("text") == "OFF":

            if strategy_selected == 'Technical':
                new_strategy = TechnicalStrategy(contract, timeframe, balance_pct, take_profit, stop_loss, self._additional_parameters[b_index])
            elif strategy_selected == 'Brakeout':
                new_strategy = BrakeoutStrategy(contract, timeframe, balance_pct, take_profit, stop_loss, self._additional_parameters[b_index])
            else:
                return

            new_strategy.candles = self.binance.get_historical_candles(contract, timeframe)

            if len(new_strategy.candles) == 0:
                self.root.logging_frame.add_log(f"No historical candle retrieved for {contract.symbol}")
                return

            self.binance.subscribe_channel([contract], "aggTrade")

            self.binance.strategies[b_index] = new_strategy

            for param in self._base_params:
                code_name = param['code_name']

                if code_name != "activation" and "_var" not in code_name:
                    self.body_widget[code_name][b_index].config(state=tk.DISABLED)

            self.body_widget['activation'][b_index].config(bg="darkgreen", text="ON")
            self.root.logging_frame.add_log(f"{strategy_selected} strategy on {symbol}/{timeframe} started")
        else:
            del self.binance.strategies[b_index]

            for param in self._base_params:
                code_name = param['code_name']

                if code_name != "activation" and "_var" not in code_name:
                    self.body_widget[code_name][b_index].config(state=tk.NORMAL)

            self.body_widget['activation'][b_index].config(bg="darkred", text="OFF")
            self.root.logging_frame.add_log(f"{strategy_selected} strategy on {symbol}/{timeframe} stoped")




    def _delete_row(self, b_index: int):
        for element in self._base_params:
            self.body_widget[element['code_name']][b_index].grid_forget()
            del self.body_widget[element['code_name']][b_index]