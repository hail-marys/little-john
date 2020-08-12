import json

companies = open('companies.txt', 'r')
tickers = open('tickers.txt', 'r')

companies_list = []
tickers_list = []

for i in companies.readlines():
    companies_list.append(i[0:len(i)-1])

for i in tickers.readlines():
    tickers_list.append(i[0:len(i)-1])


dictionary = {tickers_list[i]: companies_list[i] for i in range(len(tickers_list))}
print(dictionary)

companies.close()
tickers.close()

with open('sp500_companies.json', 'w+') as file:
    file.write(json.dumps(dictionary))
