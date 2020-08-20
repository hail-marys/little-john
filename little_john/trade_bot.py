import sys
import finnhub
import config
import schedule
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class Trade_Bot:
    """turns tradebot on and off, default initialization is off
    """

    def __init__(self):
        self.status = 'off'
        self.client = finnhub.Client(config.api_key)
        self.message = 'None'
        self.data = self.open_json('user_data/target_list.json')

    def turn_on_or_off(self):
        """ask if you want to turn bot on or off
        """
        if self.status == 'off':
            self.status = 'on'
        elif self.status == 'on':
            self.status = 'off'

    def plan_b(self):
        """
        This is in case the prediction algorithm is out.

        Args:
            sym ([str]): [the Symbol to the company]
        """
        from statistics import mean
        from little_john.search_stocks import SearchStocks
        import little_john.prediction_algorithm as pd
        search = SearchStocks()
        for i in self.data['companies']:
            o = search.candle(i)
            v = mean(o['c'])
            avg_close = round(v, 2)
            trg = pd.get_prediction(i)
            self.trade_algorithm(i, trg, avg_close)

    def trade_algorithm(self, sym=None, op=None, cl=None):
        """
        This starts the trade

        Args:
            sym ([str], optional): [Symbol of stock]. Defaults to None.
            open ([str], optional): [the open price]. Defaults to None.
        """
        self.conditional(sym, op, cl)

    def open_json(self, file):
        """
        Opens JSON file

        Args:
            file ([str]): [json file path]

        Returns:
            [dict]: [Dictionary of the json file opened]
        """
        import json
        with open(file, 'r+') as f:
            targets = json.load(f)
        return targets

    def conditional(self, sym, op, cl):
        """
        evaluates if stock should be sold or bought.

        Args:
            sym ([str]): [symbol]
            op ([str]): [open price]
        """

        current = int(self.client.quote(sym)['c'])
        # print(current)
        if current <= op:
            # or current <= cl(CONDITIONAL FOR THE PREDICT)
            #  or eom >= .05
            print('BUYING')
            self.buy_stock(sym, 500)
            self.alert(sym, 500, 'bought')
        elif current >= op and current in self.open_json('user_data/target_list.json'):
            # or current >= cl (CONDITIONAL FOR THE PREDICT)
            #  or eom <= .02
            print('SELLING')
            self.sell_stock(sym)
            self.alert(sym, 500, 'sold')
        else:
            return

    def buy_stock(self, sym, amt):
        """
        Calls methods to  run  add.

        Args:
            sym ([str]): [stock symbol]
            amt ([int]): [the amount to buy]
        """
        from little_john.manual_trade import Manual_trade
        trader = Manual_trade()
        trader.check(sym)
        trader.buy('buy')
        trader.amount_of(amt)
        trader.confirmation('y')

    def sell_stock(self, sym):
        """
        Sells the stock

        Args:
            sym ([sym]): [Stock symbol]
        """
        from little_john.view_trades import View_trades
        seller = View_trades()
        seller.selling(sym)

    def alert(self, sym, amt, trans):
        """
        alert what stock was bought

        Args:
            sym ([type]): [description]
            amt ([type]): [description]
            trans ([type]): [description]
        """
        print(f'R2D2 {trans} {amt} of {sym} shares')
        self.message = f'R2D2 {trans} {amt} of {sym} shares'


# bot = Trade_Bot()

# bot.trade_algorithm()
