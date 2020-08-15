import finnhub
from little_john.broker import Broker
import sys


class Manual_trade():
    """
    Manual trade class that has methods for handling trades
    """

    def __init__(self):
        """
        holds all the values that we want to right to the JSON file
        """
        self.client = finnhub.Client(api_key="brqm9efrh5rce3ls8mdg")
        self.symbol = None
        self.company = None
        self.buy_or_trade = None
        self.amount = None
        self.current = None

    def check(self, sym):
        """
        checks if company exists and processes it with company proccess

        Args:
            sym str: stock symbol from the main menu.

        Returns:
            function: return either the menu or processes the company
        """
        data = self.client.company_profile(symbol=sym)
        if data == {}:
            print('That was the wrong input')
            return self.menu()
        else:
            self.current = self.client.quote(sym)['c']
            self.process_company(data)

    def menu(self):
        """
        Runs inputs one by one and stores the data into class, writes all data to JSON file.
        """
        company = input('Which Company? Enter symbol:\n').upper()
        self.check(company)

        entry = input('Buy or Short?\n').lower()
        self.buy(entry)

        amt = input('How much?\n')
        self.amount_of(amt)

        confirm = input('Confirm? Enter y or n\n')
        self.confirmation(confirm)

    def process_company(self, comp):
        """
        Assigns name and symbol to the class.

        Args:
            comp -> dict: Contains data on the company.
        """
        self.company = comp['name']
        self.symbol = comp['ticker']

    def buy(self, decsion):
        """
        Finds out if you want to buy or trade.

        Args:
            decsion str: either yes or no
        """
        decsion.lower()
        if decsion == 'buy' or decsion == 'short':
            self.buy_or_trade = decsion
        else:
            print('Invalid input')
            entry = input('Buy or Short?\n').lower()
            self.buy(entry)

    def amount_of(self, amt):
        """
        Assigns the amount bought to the amount value in the class.

        Args:
            amt str: This is the amount that you want from the broker.
        """
        self.amount = amt

    def confirmation(self, entry):
        """
        Takes all the data and appends it to the JSON file for the view trades to reference

        # TODO: can't enter duplicate values.

        Args:
            entry str: takes yes or no
        """

        import json
        shares = int(self.amount) / int(self.current)

        new_data = {self.symbol: {
            "name": self.company,
            "symbol": self.symbol,
            "typeOfBuy": self.buy_or_trade,
            "currentAtPurchase": self.current,
            "invested": self.amount,
            "shares": round(shares, 2)
        }
        }
        entry.lower()
        if entry == 'y':
            from little_john.broker import Broker
            broke = Broker()
            amt = self.amount
            broke.remove_funds(int(amt))
            with open('logs/trades.json', 'r+') as f:
                data = json.load(f)
                data.update(new_data)
                f.seek(0)
                json.dump(data, f)
        elif entry == 'n':
            # TODO: come up with something better to return
            return
        else:
            print('Invalid input')
            confirm = input('Confirm? Enter yes or no\n')
            self.confirmation(confirm)
