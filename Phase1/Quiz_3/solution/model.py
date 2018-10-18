import json
import mapper
from wrapper import Markit
import requests


def buy(user_id, ticker_symbol, trade_volume):
    pass

def sell():
    pass

def lookup(company_name):
    # endpoints = 'http://dev.markitondemand.com/MODApis/Api/v2'
    # response = json.loads(requests.get(endpoint).text)
    # return response[0]['Symbol']
    with Markit() as m:
        return m.lookup(company_name)

def quote(ticker_symbol):
    with Markit() as m:
        return m.quote(ticker_symbol)

if __name__ == '__main__':
    # Simple Test
    print('This is the price of tesla: ',quote(lookup('tesla')))