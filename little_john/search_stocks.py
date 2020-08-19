
import finnhub
import requests
import os
import config
import pyfiglet
from termcolor import colored, cprint


class SearchStocks:

    def __init__(self):
        """Hold API key"""
        self.client = finnhub.Client(config.api_key)

    def menu(self):
        """Allows user to enter a company and displays values"""
        os.system('clear' if os.name == 'nt' else 'clear')
        title = pyfiglet.figlet_format('SEARCH FOR STOCKS')
        print(title)
        entry = input(
            'Which company would you like to search for? Enter symbol:\n').upper()
        cprint(entry, 'yellow')
        if self.check(entry):
            self.current_stock_price(entry)
            self.open_stock_price(entry)
            self.high_stock_price(entry)
            self.low_stock_price(entry)
            self.market_cap(entry)
            self.week_high(entry)
            self.week_low(entry)
            self.pe_ratio(entry)
            self.div_yield(entry)
            i = input('\nPress any key to return to the main menu')
        else:
            print(f'That company symbol does not exist.\n')
            self.menu()

    def check(self, entry):
        """Checks to see if company entered is valid"""
        data = self.client.company_profile(symbol=entry)
        if data == {}:
            return False
        else:
            return True

    def current_stock_price(self, symbol):
        """Gets current stock price"""
        current = self.client.quote(symbol)['c']
        print(f'Current Stock Value: {current}')
        return f'Current Stock Value: {current}'

    def open_stock_price(self, symbol):
        """Gets stock price at open"""
        open = self.client.quote(symbol)['o']
        print(f'Open: {open}')
        return f'Open: {open}'

    def high_stock_price(self, symbol):
        """Gets highest stock price of the day"""
        high = self.client.quote(symbol)['h']
        print(f'High: {high}')
        return f'High: {high}'

    def low_stock_price(self, symbol):
        """Gets lowest stock price"""
        low = self.client.quote(symbol)['l']
        print(f'Low: {low}')
        return f'Low: {low}'

    def market_cap(self, symbol):
        """Gets market cap for company"""
        cap = self.client.company_profile(
            symbol=symbol)['marketCapitalization']
        print(f'Market Capitalization: {cap}')
        return f'Market Capitalization: {cap}'

    def week_high(self, symbol):
        """Gets 52-week high"""
        high = self.client.company_basic_financials(
            symbol, 'all')['metric']['52WeekHigh']
        print(f'52 week high: {high}')
        return f'52 week high: {high}'

    def week_low(self, symbol):
        """Gets 52-week low"""
        low = self.client.company_basic_financials(
            symbol, 'all')['metric']['52WeekLow']
        print(f'52 week low: {low}')
        return f'52 week low: {low}'

    def pe_ratio(self, symbol):
        """Get P/E ratio trailing twelve months"""
        ratio = self.client.company_basic_financials(
            symbol, 'all')['metric']['pfcfShareTTM']
        print(f'P/E ratio: {ratio}')
        return f'P/E ratio: {ratio}'

    def div_yield(self, symbol):
        """Get annual div yield"""
        div = self.client.company_basic_financials(
            symbol, 'all')['metric']['dividendYieldIndicatedAnnual']
        print(f'DIV yield: {div}')
        return f'DIV yield: {div}'

    def candle(self, symbol):
        """Candle stick data for bot, pulled data from each day between 8/12/2019 1pm - 8/12/2020 1pm"""
        candle = self.client.stock_candles(symbol, 'D', 1593610200, 1596225600)
        # print(f'{candle}')
        return candle


# search = SearchStocks()
# search.menu()
# search.current_stock_price('AAPL')
# search.open_stock_price('AAPL')
# search.high_stock_price('AAPL')
# search.low_stock_price('AAPL')
# search.market_cap('AAPL')
# search.week_high('AAPL')
# search.week_low('AAPL')
# search.pe_ratio('AAPL')
# search.div_yield('AAPL')
"""For bot function"""
# o = search.candle('AAPL')
# v = mean(o['c'])
# print(round(v, 2))
