import json


class Broker():
    """
    Instance to add fake funds, remove (spend) fake funds, and return user's balance.
    Broker intializes with the balance in the user_balance.json file.
    Methods to add or remove funds updates the user_balance.json file.
    This gives memory to the current account balance, but also means that tests 
    to increase/decrease balance need to be carefully managed.
    """

    def __init__(self):
        try:
            with open('../logs/user_balance.json', 'r') as file:
                response = json.load(file)
                self.balance = response['balance']
        except FileNotFoundError:
            with open('logs/user_balance.json', 'r') as file:
                response = json.load(file)
                self.balance = response['balance']

    def add_funds(self, amount):
        self.balance += amount
        self.update_user_balance_json()

    def remove_funds(self, amount):
        self.balance -= amount
        self.update_user_balance_json()

    def update_user_balance_json(self):
        try:
            with open('../logs/user_balance.json', 'w+') as file:
                file.write(json.dumps({

                    "balance": self.balance

                }))
        except FileNotFoundError:
            with open('logs/user_balance.json', 'w+') as file:
                file.write(json.dumps({

                    "balance": self.balance
                }))


# every time a stock trade happens
# logs to json file for transaction.json and history.json file

if __name__ == "__main__":
    broker = Broker()
    # ! uncommenting below will permanently add funds to json file
    # broker.add_funds(1000)
    print(broker.balance)
