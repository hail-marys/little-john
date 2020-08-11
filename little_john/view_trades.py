import json


class View_trades:

    """
    This shows all your trades
    """

    def __init__(self, file):
        with open(file, 'r') as trades:
            trade = json.load(trades)

            self.data = trade

    def __repr__(self):
        return f'data: {self.data} '

    def display(self):
        """
        Display stocks from json file
        """
        for i in self.data:
            print(f'\nName: {self.data[i]["name"]}')
            print(f'Symbol: {self.data[i]["symbol"]}')
            print(f'Current: {self.data[i]["current"]}')
            print(f'Invested: {self.data[i]["invested"]}')
            print(f'Change: {self.data[i]["pctChanged"]}\n')
