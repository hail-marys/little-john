import finnhub
import datetime
import json

class View_Trade_History:
    """this class will generate the trade history
    """
    def __init__(self, name, symbol, date):
        self.name = name
        self.symbol = symbol 
        self.date = date
    
    def __repr__(self):
        return f'"name": {self.name}, "symbol": {self.symbol},"date": {self.date}'  

    def display_history(self):
        """
        Display trading history from json file
        """
        for i in range(len(self.name)):
            print(f'Name: {self.name[i]}')
            print(f'Symbol: {self.symbol[i]}')
            print(f'Date: {self.date[i]}')
        
        
    

