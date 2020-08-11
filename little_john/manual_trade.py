import finnhub
from little_john.broker import Broker
import sys

finnhub_client = finnhub.Client(api_key="brqm9efrh5rce3ls8mdg")

# print(finnhub_client.company_profile(symbol='fdsfae'))


class Manual_trade():
    """
    Manual trade class that has methods for handling trades
    """

    # TODO: add key name to file

    def __init__(self):
        self.client = finnhub.Client(api_key="brqm9efrh5rce3ls8mdg")
        self.symbol = None
        self.company = None
        self.buy_or_trade = None
        self.amount = None

    def check(self, sym):
        data = finnhub_client.company_profile(symbol=sym)
        print(data)

        if data == {}:
            print('That was the wrong input')
            return self.menu()
        else:
            self.process_company(data)

    def menu(self):
        company = input('Which Company? Enter symbol:\n').upper()
        self.check(company)

        entry = input('Buy or Short?\n').lower()
        self.buy(entry)

        amt = input('How much?\n')
        self.amount_of(amt)

        confirm = input('Confirm? Enter yes or no\n')
        self.confirmation(confirm)

    def process_company(self, comp):
        self.company = comp['name']
        self.symbol = comp['ticker']

    def buy(self, decsion):
        decsion.lower()
        if decsion == 'buy' or decsion == 'short':
            self.buy_or_trade = decsion
        else:
            print('Invalid input')
            entry = input('Buy or Short?\n').lower()
            self.buy(entry)

    def amount_of(self, amt):
        self.amount = amt

    def confirmation(self, entry):
        import json
        new_data = {self.symbol: {
            "name": self.company,
            "symbol": self.symbol,
            "current": "something",
            "invested": self.amount,
            "pctChanged": "percentage"
        }
        }
        entry.lower()
        if entry == 'yes':
            with open('logs/trades.json', 'r+') as f:
                data = json.load(f)
                data.update(new_data)
                f.seek(0)
                json.dump(data, f)
        elif entry == 'no':
            # TODO: come up with something better to return
            return
        else:
            print('Invalid input')
            confirm = input('Confirm? Enter yes or no\n')
            self.confirmation(confirm)


# trade = Manual_trade()

# trade.check('TSLA')

# trade.menu()
# print(trade.company)
