import requests
import json

class Api_quote:
    def __init__(self):
        self.base_url = 'http://dev.markitondemand.com/MODApis/Api/v2/'
        self.quote_url = 'Quote/json?symbol='

    def quote(self, symbol):
        api_call = self.base_url + self.quote_url + symbol
        response = json.loads(requests.get(api_call).text)
        print(response)
        return response