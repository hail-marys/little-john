import finnhub
from little_john.broker import Broker

finnhub_client = finnhub.Client(api_key="brqm9efrh5rce3ls8mdg")

# print(finnhub_client.company_profile(symbol='AAPL'))


class ManualTrade():
    """
    Manual trade class that has methods for handling trades
    """

    # TODO: add key name to file

    def __init__(self):
        self.client = finnhub.Client(api_key="brqm9efrh5rce3ls8mdg")
        self.company = None
        self.buy = None
        self.amount = None

    def check(self, sym):
        data = finnhub_client.company_profile(symbol=sym)
        if data == None:
            print('That was the wrong input')
            return self.menu()
        else:
            self.process_company(data)

    def menu(self):
        company = input('Which Company? Enter symbol:\n')
        company.upper()
        self.check(company)

        # buy = input('Buy or Short?\n')

        # amount = input('How much?\n')

        # Confirm = input('Confirm? Enter yes or no\n')

    def process_company(self, comp):
        self.company = comp['name']


trade = ManualTrade()

trade.menu()
print(trade.company)
