import finnhub
import json


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
        for i in self.data:
            print(f'\nName: {self.data[i]["name"]}')
            print(f'Symbol: {self.data[i]["symbol"]}')
            print(f'TypeOfBuy: {self.data[i]["typeOfBuy"]}')
            print(f'Invested: {self.data[i]["invested"]}')
            print(f'Shares: {self.data[i]["shares"]}')
            print(f'Date_Purchased: {self.data[i]["date_purchased"]}\n')
        i = input('Press any key to exit')


if __name__ == "__main__":
    test = View_Trade_History('./logs/trade_history.json')
    test.display_history()
