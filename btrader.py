import pandas as pd
from API.alphavantage import AlphaVantage
from config.config import *

import history
from dateutil.parser import parse
import pytz

local_tz = pytz.timezone('Europe/Istanbul')


def utc_to_local(utc_dt):
    utc_dt = parse(utc_dt)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    temp = local_tz.normalize(local_dt)
    temp = str(temp).replace('+03:00', '')
    return temp


class Response():
    def __init__(self):
        self.responses = []

    def set_response(self, text):
        self.responses.append(text)

    def get_response(self):
        text = ""
        if self.responses:
            for i in self.responses:
                text += i.replace('+03:00', '') + '\n'
        return text


class BTrader():
    def __init__(self, id):
        self.av = AlphaVantage(ALPHA_VANTAGE_API_KEY)
        self.id = id
        self.response = Response()
       
        self.bar_period = selected_tf

    def run(self):
        prices = pd.read_csv(self.av.get_intraday_crypto(
            ticker, self.bar_period), index_col='timestamp')[0:25].iloc[::-1]
        daily = pd.read_csv(self.av.get_crypto_daily_sma(
            ticker), index_col='time')[0:1]

        op = []
        latestDelta = None
        for i in prices['close']:
            if latestDelta:
                delta = abs(i - daily['SMA'].values[0])
                if delta < latestDelta:
                    op.append({'date': utc_to_local(
                        prices[prices['close'] == i].index.values[0]), 'delta': delta, 'val': i})
            latestDelta = abs(i - daily['SMA'].values[0])

        if op:
            if(history.search_history(self.id, op)):
                history.set_history(self.id, op)
                self.response.set_response(
                    '\n10 günlük ortalamaya yaklaşan değerler:')
                for i in op:
                    self.response.set_response(
                        f"\n{i['date']} saatinde:  10 günlük ortalamaya {i['delta']} USD kadar yaklaşıldı. Değeri ise {i['val']}")
            else:
                self.response.set_response(
                    '\n10 günlük ortalamaya hiç yaklaşım olmadı.')
        else:
            self.response.set_response(
                '\n10 günlük ortalamaya hiç yaklaşım olmadı.')
