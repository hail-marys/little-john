import json


class viewTrades:
    """
    This shows all your trades
    """

    def __init__(self, file):
        with open(file, 'r') as trades:
            trade = json.load(trades)

            self.name = trade['name']
            self.symbol = trade['symbol']
            self.current = trade['current']
            self.invested = trade['invested']
            self.change = trade['pctChanged']

    def __repr__(self):
        return f'"name": {self.name}, "symbol": {self.symbol}, "current": {self.current}, "invested": {self.invested},"pctChanged": {self.change} '

    def display(self):
        """
        Display stocks from json file
        """
        for i in range(len(self.name)):
            print(f'\nName: {self.name[i]}')
            print(f'Symbol: {self.symbol[i]}')
            print(f'Current: {self.current[i]}')
            print(f'Invested: {self.invested[i]}')
            print(f'Change: {self.change[i]}\n')
