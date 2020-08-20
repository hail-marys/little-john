from little_john.search_stocks import SearchStocks
from little_john.search_stocks import finnhub

def test_search_stocks_class_exists():
    assert SearchStocks

def test_current_stock_price():
    ss = SearchStocks()
    actual = ss.current_stock_price('AAPL')
    expected = f'Current Stock Value: 460.04'
    assert actual == expected 


def test_open_stock_price():
    ss = SearchStocks()
    actual = ss.open_stock_price('AAPL')
    expected = f'Open: 457.72'
    assert actual == expected 


def test_high_stock_price():
    ss = SearchStocks()
    actual = ss.high_stock_price('AAPL')
    expected = f'High: 464.145'
    assert actual == expected


def test_low_stock_price():
    ss = SearchStocks()
    actual = ss.low_stock_price('AAPL')
    expected = f'Low: 455.71'
    assert actual == expected



def test_market_cap():
    ss = SearchStocks()
    actual = ss.market_cap('AAPL')
    expected = f'Market Capitalization: 1927926'
    assert actual == expected


def test_week_high():
    ss = SearchStocks()
    actual = ss.week_high('AAPL')
    expected = f'52 week high: 457.65'
    assert actual == expected


def test_week_low():
    ss = SearchStocks()
    actual = ss.week_low('AAPL')
    expected = f'52 week low: 199.15'
    assert actual == expected


def test_pe_ratio():
    ss = SearchStocks()
    actual = ss.pe_ratio('AAPL')
    expected = f'P/E ratio: 32.9588'
    assert actual == expected


def test_div_yield():
    ss = SearchStocks()
    actual = ss.div_yield('AAPL')
    expected = f'DIV yield: 0.73799'
    assert actual == expected

