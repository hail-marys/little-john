from little_john.broker import Broker
import json


def test_broker_class_exists():
    assert Broker


def test_return_balance():
    test_broker = Broker()
    test_broker.add_funds(10000)
    with open('logs/user_balance.json', 'r') as file:
        response = json.load(file)
        assert response['balance'] == 10000

    # prevent messing up the user_balance.json file
    # by removing the funds added
    test_broker.remove_funds(10000)


def test_add_funds():
    test_broker = Broker()
    old_balance = test_broker.balance
    test_broker.add_funds(1000)
    assert test_broker.balance == old_balance + 1000

    # prevent messing up the user_balance.json file
    # by removing the funds added
    test_broker.remove_funds(1000)


def test_remove_funds():
    test_broker = Broker()
    old_balance = test_broker.balance
    test_broker.remove_funds(1000)
    assert test_broker.balance == old_balance - 1000

    # prevent messing up the user_balance.json file
    # by adding the funds removed
    test_broker.add_funds(1000)


