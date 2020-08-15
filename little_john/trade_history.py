import finnhub
import json


class View_Trade_History:
    """this class will generate the trade history
    """

    def __init__(self, file):
        with open(file, 'r') as history:
            trade_history = json.load(history)
            self.data = trade_history
            print(trade_history)
            

    def __repr__(self):
        """This method returns the string representation of the object
        """
        return f'"name": {self.name}, "symbol": {self.symbol},"amount": {self.amount},"shares": {self.number_of_shares},"date_purchased": {self.start_date}'


    def display_history(self):
        """
        Display data will be pulled from json file
        """
        for i in range(len(self.data)):
            print(f'\nName: {self.data[i]["name"]}')
            print(f'Symbol: {self.data[i]["symbol"]}')
            print(f'TypeOfBuy: {self.data[i]["typeOfBuy"]}')
            print(f'Invested: {self.data[i]["invested"]}')
            print(f'Shares: {self.data[i]["shares"]}')
            print(f'Date_Purchased: {self.data[i]["name"]}\n')


if __name__ == "__main__":
    test = View_Trade_History('./logs/trade_history.json')
    test.display_history()
