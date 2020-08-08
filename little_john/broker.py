
class Broker():
    """
    Instance to add fake funds, remove (spend) fake funds, and return user's balance.
    """

    def __init__(self, balance=0):
        self.balance = balance

    def add_funds(self, amount):
        self.balance += amount

    def remove_funds(self, amount):
        self.balance -= amount


# every time a stock trade happens
# logs to json file for transaction.json and history.json file
# 