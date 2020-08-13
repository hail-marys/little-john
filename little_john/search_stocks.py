import finnhub
import requests

# finnhub_client = finnhub.Client(api_key='brqm9efrh5rce3ls8mdg')

# r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=')
# print(r.json())


def start():
    run = True
    while run:
        display_text('AAPL')
        ipt = input('> ')
        if ipt == 'quit':
            sys.exit('main_menu')
        else:
            print('Please search for a company')


def display_text(symbol):
    print(f'Which company would you like to search for? Enter symbol:')


# start()


class SearchStocks:

    def __init__(self):
        self.client = finnhub.Client(api_key='brqm9efrh5rce3ls8mdg')


    def menu(self):
        entry = input(f'Which company would you like to search for? Enter symbol: ')
        self.current_stock_price(entry)


    def current_stock_price(self, symbol):
        """Gets current stock price"""
        current = self.client.quote(symbol)['c']
        # print(self.client.quote(symbol))
        print(f'Current Stock Value: {current}')
    

    def open_stock_price(self, symbol):
        """Gets stock price at open"""
        open = self.client.quote(symbol)['o']
        # print(self.client.quote(symbol))
        print(f'Open: {open}')


    def high_stock_price(self, symbol):
        """Gets highest stock price of the day"""
        high = self.client.quote(symbol)['h']
        # print(self.client.quote(symbol))
        print(f'High: {high}')


    def low_stock_price(self, symbol):
        """Gets lowest stock price"""
        low = self.client.quote(symbol)['l']
        # print(self.client.quote(symbol))
        print(f'Low: {low}')


    def market_cap(self, symbol):
        """Gets market cap for company"""
        cap = self.client.company_profile(symbol=symbol)['marketCapitalization']
        # print(self.client.company_profile(symbol))
        print(f'Market Capitalization: {cap}')

# print(finnhub_client.company_basic_financials('AAPL', 'margin'))
    def basic_financials(self, symbol):
        """Gets basic financials such as margin, P/E ratio, 52-week high/low"""
        basic = self.client.company_basic_financials(symbol, 'metric')
        # print(self.client.company_profile(symbol))
        print(f'Basic Financials: {basic}')



search = SearchStocks()
search.current_stock_price('AAPL')
search.open_stock_price('AAPL')
search.high_stock_price('AAPL')
search.low_stock_price('AAPL')
search.market_cap('AAPL')
search.basic_financials('AMZN')