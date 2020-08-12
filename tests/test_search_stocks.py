from little_john.search_stocks import SearchStocks
from little_john.search_stocks import finnhub

def test_search_stocks_class_exists():
    assert SearchStocks


def test_current_stock_price():
    test_cst = SearchStocks()
    test_cst.insert(self, 'AAPL')
    assert test_cst == 'AAPL'


