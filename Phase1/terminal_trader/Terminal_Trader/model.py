#!/usr/bin/env python3

import json
from mapper import Database
from wrapper import Markit
import requests
import time

m = Markit()

def sign_up(user_id, password):
    with Database('TRADER.db') as db:
        db.signup(user_id,password)

def check_balance(user_id):
    with Database('TRADER.db') as db:
        bal = db.check_balance(user_id)
        return bal

def login(_user_id, _password):
    with Database('TRADER.db') as db:
        return db.loggin(_user_id, _password)

def buy(user_id,ticker_symbol,trade_volume):
    sell_buy = 'Buy'
    trade_price = m.quote(ticker_symbol)
    total = float(trade_volume) * trade_price
    with Database('TRADER.db') as db:
        if total <= db.check_balance(user_id):
            db.add_buy(user_id, sell_buy, ticker_symbol, trade_price, trade_volume, total)
            print('You bought ' + ticker_symbol + ' amount of ' + str(trade_volume) + ' and the total you spent is '+ str(total))
            old_balance = db.check_balance(user_id)
            new_balance = old_balance - total
            db.change_balance(user_id,new_balance)
            try:
                if None == db.fetch_all(user_id, ticker_symbol):
                    db.insert_portfolio(user_id, ticker_symbol, trade_volume)
                else:
                    company_volume = db.fetch_volume(user_id,ticker_symbol)
                    company_volume += float(trade_volume)
                    db.update_portfolio(user_id, ticker_symbol, company_volume)
            except TypeError:
                db.insert_portfolio(user_id, ticker_symbol, trade_volume)
        else:
            print('Not enought money.')

def sell(user_id,ticker_symbol,trade_volume):
    sell_buy = 'Sell'
    trade_price = m.quote(ticker_symbol)
    total = float(trade_volume) * trade_price
    with Database('TRADER.db') as db:
        if db.fetch_volume(user_id, ticker_symbol) >= float(trade_volume):
            db.add_sell(user_id, sell_buy, ticker_symbol, trade_price, trade_volume, total)
            print('You sold ' + ticker_symbol + ' amount of ' + str(trade_volume) + ' and the total you earned is '+ str(abs(total)))
            old_balance = db.check_balance(user_id)
            new_balance = old_balance + total
            db.change_balance(user_id,new_balance)
            company_volume = db.fetch_volume(user_id,ticker_symbol)
            company_volume -= float(trade_volume)
            db.update_portfolio(user_id, ticker_symbol, company_volume)
        else:
            print('You don\'t have enough company volume.')

def lookup(company_name):
    return m.lookup(company_name)


def quote(ticker_symbol):
    return m.quote(ticker_symbol)


# if __name__ == '__main__':
#     buy('kkim','IBM', 10)
    # print(db.fetch_symbol('kkim','IBM'))
    # ticker_symbol = 'TSLA'
    # user_id = 'kkim'
    # print(db.fetch_volume(user_id,ticker_symbol))
    # if str(ticker_symbol) == str(db.fetch_symbol(user_id)) and str(user_id) == str(db.fetch_id(ticker_symbol)):
    #     print('1')