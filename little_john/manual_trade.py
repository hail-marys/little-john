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
        self.company = None
        self.buy_or_trade = None
        self.amount = None

    def check(self, sym):
        data = finnhub_client.company_profile(symbol=sym)

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

        # amount = input('How much?\n')

        # Confirm = input('Confirm? Enter yes or no\n')

    def process_company(self, comp):
        self.company = comp['name']

    def buy(self, decsion):
        decsion.lower()
        if decsion == 'buy' or decsion == 'short':
            self.buy_or_trade = decsion
        else:
            print('Invalid input')
            entry = input('Buy or Short?\n').lower()
            self.buy(entry)


# trade = ManualTrade()

# trade.menu()
# print(trade.company)
