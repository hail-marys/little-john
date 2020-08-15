import sys
import finnhub
import config
import schedule
import time


class Trade_Bot:
    """turns tradebot on and off, default initialization is off
    """

    def __init__(self):
        self.status = 'off'
        self.client = finnhub.Client(config.api_key)

    def turn_on_or_off(self):
        """ask if you want to turn bot on or off
        """
        if self.status == 'off':
            self.status = 'on'
        elif self.status == 'on':
            self.status = 'off'

    def trade_algorithm(self, sym=None, open=None, high=None, low=None, eom=None):

        while self.status == 'on':
            import threading
            # for i in target list:
            # sym = Prediction_algorithm.sym()
            # open = Prediction_algorithm.open()
            # high = Prediction_algorithm.high()
            # low = Prediction_algorithm.low()
            # eom = Prediction_algorithm.eom()
            # hr = 3600.0 sec

            starttime = time.time()
            print('TICK')
            # self.conditional(sym, low, high, eom)
            time.sleep(30.0 - ((time.time() - starttime) % 60.0))

    def conditional(self, sym, low, high, eom):
        current = int(self.client.quote(sym)['c'])
        if current <= low or eom >= .05:
            print('BUYING')
            self.buy_stock(sym, 500)
            self.alert(sym, 500, 'bought')
        elif current >= high or eom <= .02:
            print('SELLING')
            self.sell_stock(sym)
            self.alert(sym, 500, 'sold')
        else:
            return

    def buy_stock(self, sym, amt):
        from little_john.manual_trade import Manual_trade
        trader = Manual_trade()
        trader.check(sym)
        trader.buy('buy')
        trader.amount_of(amt)
        trader.confirmation('y')

    def sell_stock(self, sym):
        from little_john.view_trades import View_trades
        seller = View_trades()
        seller.selling(sym)

    def alert(self, sym, amt, trans):
        print(f'R2D2 {trans} {amt} of {sym} shares')
        return f'R2D2 {trans} {amt} of {sym} shares'


trade = Trade_Bot()
trade.status = 'off'

trade.trade_algorithm()

"""
Method to run the algorithm
* Symbol
* open month
* high month
* low month
* eom month

Condition for when to buy
    * how much to buy
    * buy when close to month low
    * or when eom pct is greater than <value>
Condition for when to sell
    * sell when above high or above eom pct for current and at purchase
    * if exceeds low sell
invterval check on bought stocks to sell
    * every hr eval sell
Live alert on the main pages showing when stocks are bought or sold
    * when a condition is met return results to main.py


"""


# if __name__ == "__main__":
#     test = Trade_Bot('./trade_history.json')
#     test.turn_on_or_off()
