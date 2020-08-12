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
        print(f'Current Stock Value: {current}')
    

    def open_stock_price(self, symbol):
        """Gets stock price at open"""
        open = self.client.quote(symbol)['o']
        print(f'Open: {open}')


    def high_stock_price(self, symbol):
        """Gets highest stock price of the day"""
        high = self.client.quote(symbol)['h']
        print(f'High: {high}')


    def low_stock_price(self, symbol):
        """Gets lowest stock price"""
        low = self.client.quote(symbol)['l']
        print(f'Low: {low}')


    def market_cap(self, symbol):
        """Gets market cap for company"""
        cap = self.client.company_profile(symbol=symbol)['marketCapitalization']
        print(f'Market Capitalization: {cap}')


    def week_high(self, symbol):
        """Gets 52-week high"""
        high = self.client.company_basic_financials(symbol, 'all')['metric']['52WeekHigh']
        print(f'52 week high: {high}')


    def week_low(self, symbol):
        """Gets 52-week low"""
        low = self.client.company_basic_financials(symbol, 'all')['metric']['52WeekLow']
        print(f'52 week low: {low}')


    def pe_ration(self, symbol):
        """Get P/E ratio trailing twelve months"""
        ratio = self.client.company_basic_financials(symbol, 'all')['metric']['pfcfShareTTM']
        print(f'P/E ratio: {ratio}')


    def div_yield(self, symbol):
        """Get annual div yield"""
        div = self.client.company_basic_financials(symbol, 'all')['metric']['dividendYieldIndicatedAnnual']
        print(f'DIV yield: {div}')

    
    def candle(self, symbol):
        """Candle stick data for bot, pulled data from each day between 8/12/2019 1pm - 8/12/2020 1pm"""
        candle = self.client.stock_candles(symbol, 'D', 1565640000, 1597262400)
        # print(f'{candle}')



search = SearchStocks()
search.current_stock_price('AAPL')
search.open_stock_price('AAPL')
search.high_stock_price('AAPL')
search.low_stock_price('AAPL')
search.market_cap('AAPL')
search.week_high('AAPL')
search.week_low('AAPL')
search.pe_ration('AAPL')
search.div_yield('AAPL')
"""For bot function"""
# search.candle('AAPL') 