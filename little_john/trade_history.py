import finnhub
import json


class View_Trade_History:
    """this class will generate the trade history
    """

    def __init__(self, file):
        with open(file, 'r') as history:
            trade_history = json.load(history)

            self.name = trade_history['name']
            self.symbol = trade_history['symbol']
            self.amount = trade_history['amount']
            self.number_of_shares = trade_history['shares']
            self.start_date = trade_history['date_purchased']
            print(trade_history)

    def __repr__(self):
        """This method returns the string representation of the object
        """
        return f'"name": {self.name}, "symbol": {self.symbol},"amount": {self.amount},"shares": {self.number_of_shares},"date_purchased": {self.start_date}'

    def display_history(self):
        """
        Display data will be pulled from json file
        """
        for i in range(len(self.name)):
            print(f'\nName: {self.name[i]}')
            print(f'Symbol: {self.symbol[i]}')
            print(f'Amount: {self.amount[i]}')
            print(f'Shares: {self.number_of_shares[i]}')
            print(f'Date_Purchased: {self.start_date[i]}\n')


if __name__ == "__main__":
    test = View_Trade_History('./logs/trade_history.json')
    test.display_history()
