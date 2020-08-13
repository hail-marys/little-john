import json


class View_trades:

    """
    This shows all your trades
    """

    def __init__(self):
        from little_john.manual_trade import Manual_trade
        with open('logs/trades.json', 'r') as trades:
            trade = json.load(trades)

            self.data = trade
            self.quote = Manual_trade()

    def __repr__(self):
        return f'data: {self.data} '

    def display(self):
        """
        Display stocks from json file
        """

        for i in self.data:

            current_price = self.quote.client.quote(str(i))['c']
            pct_change = (int(current_price) -
                          self.data[i]["currentAtPurchase"]) / int(current_price) * 100.0
            print(f'\nName: {self.data[i]["name"]}')
            print(f'Symbol: {self.data[i]["symbol"]}')
            print(f'Current: {current_price}')
            print(f'Invested: {self.data[i]["invested"]}')
            print(f'Shares: {round(self.data[i]["shares"], 2)}')
            print(f'Change: {round(pct_change, 1)}%\n')
            # TODO: add input that allows you to sell stock
        sell = input('Would you like to sell? y or n\n')
        if sell.lower() == 'y' or sell.lower() == 'yes':
            sym = input('Which stock would you like to sell? Enter symbol\n')
            self.selling(sym.upper())
        else:
            return

    def selling(self, sym):
        # print(f'data: {self.data}')
        if self.data[sym]:
            self.delete_json(sym, self.data)
            # TODO: delete entry from json file
            # TODO: add or remove funds from broker
        else:
            print("DOESN'T EXIST")

    def delete_json(self, sym, data):
        self.talk_to_broker(sym, self.data)
        del data[sym]
        with open('logs/trades.json', 'w+') as f:
            json.dump(data, f)

    def talk_to_broker(self, sym, data):
        from little_john.broker import Broker
        broke = Broker()
        amt = data[sym]['invested']
        amt = int(amt)
        ret = self.find_share_val(sym, amt)
        new_funds = ret + amt
        broke.add_funds(new_funds)

    def find_share_val(self, sym, amt):
        shares = self.data[sym]['shares']
        curr = self.quote.client.quote(sym)['c']
        ttl = (shares * curr) - amt
        return round(ttl, 2)
