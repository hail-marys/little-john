import finnhub
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from sklearn.preprocessing import MinMaxScaler
import time
from datetime import datetime


client = finnhub.Client(api_key='brqm9efrh5rce3ls8mdg')


def get_candlestick_data(ticker, timeframe, start, end):
    data = client.stock_candles(ticker, timeframe, start, end)
    del data['s']
    df = pd.DataFrame.from_dict(data)
    df['t'] = df['t'].apply(lambda x: datetime.fromtimestamp(x))
    df = df.rename(columns={'c': 'Close', 'h': 'High', 'l': 'Low', 'o': 'Open', 't': 'Date', 'v': 'Volume'})
    df.set_index('Date', inplace=True)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    return df


def stock_data_50(ticker):
    current_time = int(time.time()) 
    prev_time = current_time - 7776000
    df = get_candlestick_data(ticker, 'D', prev_time, current_time)
    df = df.iloc[len(df)-50:]
    df = df.iloc[:, 0:1]
    return df


def get_prediction(ticker):
    data = stock_data_50(ticker)
    stock_open_data = data.iloc[:, 0:1].values
    stock_open_data = stock_open_data.reshape(-1,1)
    scaler = MinMaxScaler(feature_range = (0, 1))
    stock_open_data = scaler.fit_transform(stock_open_data)
    x_test = []
    x_test.append(stock_open_data[0:50])
    x_test = np.asarray(x_test)
    model = load_model('mdl_wts.hdf5')
    stock_prediction = model.predict(x_test)
    stock_prediction = scaler.inverse_transform(stock_prediction)
    return stock_prediction[0][0]


print(get_prediction('AAPL'))