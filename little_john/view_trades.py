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
        from little_john.manual_trade import Manual_trade

        for i in self.data:
            view = Manual_trade()
            current_price = view.client.quote(str(i))['c']
            pct_change = (int(current_price) -
                          self.data[i]["currentAtPurchase"]) / int(current_price) * 100.0
            print(f'\nName: {self.data[i]["name"]}')
            print(f'Symbol: {self.data[i]["symbol"]}')
            print(f'Current: {current_price}')
            print(f'Invested: {self.data[i]["invested"]}')
            print(f'Shares: {self.data[i]["shares"]}')
            print(f'Change: {round(pct_change, 1)}%\n')
            # TODO: add input that allows you to sell stock
        sell = input('Would you like to sell?')
        if sell.lower() == 'y' or sell.lower() == 'yes':
            sym = input('Which stock would you like to sell?')
            self.selling(sym)

    def selling(self, sym):
        pass
