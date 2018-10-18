import requests
import json
from model import Api_quote as ap
import view
from pprint import pprint
import time
import os

view.start_menu()
time.sleep(1)
a = ap()

while True:
    os.system('clear')
    view.get_quote()
    comp_name = input('\nWhat company do you want to get quote?  ')
    if comp_name.upper() == 'E':
        break
    else:
        os.system('clear')
        pprint(a.quote(comp_name))
        time.sleep(2)
        