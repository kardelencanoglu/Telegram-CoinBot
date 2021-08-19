import requests
import os

s = requests.Session()
s.trust_env = False


class AlphaVantage:
    def __init__(self, key):
        self.key = key

    def get_intraday_crypto(self, symbol, interval):
        response = requests.get(
            f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={symbol}&market=USD&interval={interval}&apikey={self.key}&datatype=csv')
        path = os.path.join('data', symbol+interval+'.csv')

        with open(path, 'w+') as f:
            f.write(response.text)
        return path

    def get_crypto_daily_sma(self, symbol):
        response = requests.get(
            'https://www.alphavantage.co/query?function=SMA&symbol={}USD&interval=daily&time_period=10&series_type=open&apikey={}&datatype=csv'.format(symbol, self.key))

        path = os.path.join('data', symbol+'USD-SMA.csv')
        with open(path, 'w+') as f:
            f.write(response.text)
        return path
