import finnhub
from little_john.broker import Broker
import sys
import json
import config
import pyfiglet
from termcolor import colored, cprint


class Manual_trade():
    """
    Manual trade class that has methods for handling trades
    """

    def __init__(self):
        """
        holds all the values that we want to right to the JSON file
        """
        self.client = finnhub.Client(config.api_key)
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
        title = pyfiglet.figlet_format('STOCK TRADES')
        print(title)
        company = input(
            'Which company would you like to trade? Enter symbol:\n').upper()
        self.check(company)

        entry = input('\nWould you like to Buy or Short?\n').lower()
        self.buy(entry)

        amt = input('\nHow much would you like to Buy/Short?\n')
        self.amount_of(amt)

        confirm = input(
            '\nAre you ABSOLUTELY sure you want to make these trades? Enter y or n\n')
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
        self.amount = int(amt)

    def confirmation(self, entry):
        """
        Takes all the data and appends it to the JSON file for the view trades to reference

        Args:
            entry str: takes yes or no
        """

        from datetime import date
        import time

        shares = int(self.amount) / int(self.current)
        today = date.today()
        today = today.strftime("%m/%d/%Y")
        unix_time = time.time()

        active = {self.symbol: {
            "name": self.company,
            "symbol": self.symbol,
            "typeOfBuy": self.buy_or_trade,
            "currentAtPurchase": self.current,
            "invested": self.amount,
            "shares": round(shares, 2)
        }
        }

        history = {int(unix_time): {
            "name": self.company,
            "symbol": self.symbol,
            "typeOfBuy": self.buy_or_trade,
            "invested": self.amount,
            "shares": round(shares, 2),
            "date_purchased": today
        }
        }

        entry.lower()
        if entry == 'y':
            from little_john.broker import Broker
            broke = Broker()
            amt = self.amount
            broke.remove_funds(int(amt))
            self.check_dup('logs/trades.json', active)
            self.save_trade('logs/trade_history.json', history)
        elif entry == 'n':
            return
        else:
            print('Invalid input')
            confirm = input('Confirm? Enter yes or no\n')
            self.confirmation(confirm)

    def save_trade(self, file, new_data):
        """
        opens and appends new data to json file

        Args:
            file JSON: Json file path
            new_data dict: dict of data to append
        """

        with open(file, 'r+') as f:
            data = json.load(f)
            data.update(new_data)
            f.seek(0)
            json.dump(data, f, indent=4)

    def check_dup(self, file, new_data):
        """
        Checks json for a duplicate value and if exists then update the dict adding the shares and invested. Gets the middle between current purchased.

        Args:
            file: path: JSON file
            new_data: dict: Object that you want to append to JSON
        """

        with open(file, 'r+') as f:
            data = json.load(f)
            key_chk = self.symbol

            if key_chk in set(data):

                share = int(self.amount) / int(self.current)
                shares_added = share + data[key_chk]['shares']

                invest = data[key_chk]['invested'] + self.amount

                curr = data[key_chk]['currentAtPurchase']
                mid = (curr + self.current) / 2
                data[key_chk].update(invested=invest)
                data[key_chk].update(shares=round(shares_added, 2))
                data[key_chk].update(currentAtPurchase=round(mid, 2))
                f.seek(0)
                json.dump(data, f, indent=4)

            else:
                self.save_trade('logs/trades.json', new_data)
