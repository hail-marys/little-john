import finnhub

finnhub_client = finnhub.Client(api_key='brqm9efrh5rce3ls8mdg')

print(finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249))

