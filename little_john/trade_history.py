import finnhub
import json
import os
import pyfiglet
from termcolor import colored, cprint


class View_Trade_History:
    """this class will generate the trade history
    """

    def __init__(self, file):
        with open(file, 'r') as history:
            trade_history = json.load(history)
            self.data = trade_history
            # print(trade_history)

    def display_history(self):
        """
        Display data will be pulled from json file
        """
        os.system('clear' if os.name == 'nt' else 'clear')
        title = pyfiglet.figlet_format('TRADE HISTORY')
        print(title)
        for i in self.data:
            print(f'\nName: {self.data[i]["name"]}')
            print(f'Symbol: {self.data[i]["symbol"]}')
            print(f'Type of buy: {self.data[i]["typeOfBuy"]}')
            print(f'Invested: {self.data[i]["invested"]}')
            print(f'Shares: {self.data[i]["shares"]}')
            print(f'Date purchased: {self.data[i]["date_purchased"]}\n')
        i = input('Press any key to exit')


if __name__ == "__main__":
    test = View_Trade_History('./logs/trade_history.json')
    test.display_history()
