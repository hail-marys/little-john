import finnhub
import tensorflow as tf
import tensorflow.keras as keras
# ! poetry add mplfinance
import mplfinance as mpf
import pandas as pd


client = finnhub.Client(api_key='brqm9efrh5rce3ls8mdg')

# July 1 through end of July 30, 21 trading days
def get_data(ticker):
    return client.stock_candles(ticker, 'D', 1593586800, 1596178800)

aapl_july = get_data('AAPL')
del aapl_july['s']


print(aapl_july)

# mpf.plot(aapl_july)

