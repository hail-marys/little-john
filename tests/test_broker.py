from little_john.broker import Broker


def test_broker_class_exists():
    assert Broker


def test_return_balance():
    test_broker = Broker(10000)
    assert test_broker.balance == 10000


def test_add_funds():
    test_broker = Broker()
    test_broker.add_funds(1000)
    assert test_broker.balance == 1000


def test_remove_funds():
    test_broker = Broker(1000)
    test_broker.remove_funds(1000)
    assert test_broker.balance == 0


