from little_john.search_stocks import SearchStocks
from little_john.search_stocks import finnhub

def test_search_stocks_class_exists():
    assert SearchStocks

def test_current_stock_price():
    ss = SearchStocks()
    actual = ss.current_stock_price('AAPL')
    expected = f'Current Stock Value: 452.04'
    assert actual == expected 


def test_open_stock_price():
    ss = SearchStocks()
    actual = ss.open_stock_price('AAPL')
    expected = f'Open: 441.99'
    assert actual == expected 

