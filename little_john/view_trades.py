import json
import pyfiglet
from termcolor import colored, cprint


class View_trades:

    """
    This shows all your trades
    """

    def __init__(self):
        """
        Pulls in trade data and the Manual trade class and stores it
        """

        from little_john.manual_trade import Manual_trade
        with open('logs/trades.json', 'r') as trades:
            trade = json.load(trades)

            self.data = trade
            self.quote = Manual_trade()

    def __repr__(self):
        return f'data: {self.data} '

    def display(self):
        """
        Display stocks from json file and takes inputs
        """
        title = pyfiglet.figlet_format('CURRENT TRADES')
        print(title)

        for i in self.data:
            current_price = self.quote.client.quote(str(i))['c']
            pct_change = (int(current_price) -
                          self.data[i]["currentAtPurchase"]) / int(current_price) * 100.0
            print(f'\nName: {self.data[i]["name"]}')
            print(f'Symbol: {self.data[i]["symbol"]}')
            print(f'Current: {current_price}')
            print(f'Invested: {self.data[i]["invested"]}')
            print(f'Shares: {round(self.data[i]["shares"], 2)}')
            print(f'Change: {round(pct_change, 1)}%\n')

        sell = input('Would you like to Sell? y or n\n')
        if sell.lower() == 'y' or sell.lower() == 'yes':
            sym = input('Which stock would you like to Sell? Enter symbol\n')
            self.selling(sym.upper())
        else:
            return

    def selling(self, sym):
        """
        Starts the selling process.

        Args:
            sym str: The stock symbol
        """
        if sym in self.data:
            self.delete_json(sym, self.data)
            i = input(f'{sym} has been sold')
        else:
            i = input("Does not exist. Press any key to try again")
            self.display()

    def delete_json(self, sym, data):
        """
        deletes data from the dict then rewrites the JSON file and talks to the broker.

        Args:
            sym str: Symbol of the stock
            data dict: Object of all the data from the trade.JSON
        """
        self.talk_to_broker(sym)
        del data[sym]
        with open('logs/trades.json', 'w+') as f:
            json.dump(data, f, indent=4)

    def talk_to_broker(self, sym):
        """
        Pull in Broker and updates it with the new funds from the sell.

        Args:
            sym str: Stock Symbol
        """
        from little_john.broker import Broker
        broke = Broker()
        amt = self.data[sym]['invested']
        ret = self.find_share_val(sym, amt)
        new_funds = ret + amt
        broke.add_funds(new_funds)

    def find_share_val(self, sym, amt):
        """
        Gets the shares from the data and the current share price. Multiplies and subtracts the amt invested.

        Args:
            sym str: Stock symbol
            amt int: number that you invested

        Returns:
            int: The number that you need to add to the amt to give to the broker.
        """
        shares = self.data[sym]['shares']
        current = self.quote.client.quote(sym)['c']
        if self.data[sym]['typeOfBuy'] == 'buy':
            ttl = (shares * current) - amt
        else:
            ttl = amt - (shares * current)

        return round(ttl, 2)
