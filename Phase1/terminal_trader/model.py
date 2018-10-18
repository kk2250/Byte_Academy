#!/usr/bin/env python3

import json
from mapper import Database
from wrapper import Markit
import requests
import pandas as pd
import numpy as np
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

def leaderboard():
    with Database('TRADER.db') as db:
        list_user = db.fetch_alluser()
        a = []
        for _ in range(len(list_user)):
            if list_user[_][0] not in a:
                a.append(list_user[_][0])
        b = []
        for __ in a:
            vol_list = db.list_volume(__)
            x = 0
            for ___ in range(len(vol_list)):
                x += m.quote(vol_list[___][2]) * vol_list[___][3]
            total_money = x + db.check_balance(__)
            b.append(total_money)
        c = []
        for ____ in range(len(b)):
            d = [a[____],b[____]]
            c.append(d)
        d = sorted(c, key=lambda x: x[1], reverse=True)
        df = pd.DataFrame(d)
        df.columns += 1
        df.index += 1
        df.columns = ['Users', 'Total money']
        return df

def view_port(user_id):
    with Database('TRADER.db') as db:
        tic = []
        for _ in range(len(db.list_volume(user_id))):
            tic.append(db.list_volume(user_id)[_][2])
        vol = []
        for __ in range(len(db.list_volume(user_id))):
            vol.append(db.list_volume(user_id)[__][3])
        val = []
        for ___ in range(len(tic)):
            val.append(vol[___]*m.quote(tic[___]))
        tot = []
        for ____ in range(len(tic)):
            t = [tic[____],vol[____], val[____]]
            tot.append(t)
        df1 = pd.DataFrame(tot)
        df1.index +=1
        df1.columns = ['Ticker symbol', 'Owned Volume', 'Money Value']
        return df1

def sum_val(user_id):
    with Database('TRADER.db') as db:
        tic = []
        for _ in range(len(db.list_volume(user_id))):
            tic.append(db.list_volume(user_id)[_][2])
        vol = []
        for __ in range(len(db.list_volume(user_id))):
            vol.append(db.list_volume(user_id)[__][3])
        val = []
        for ___ in range(len(tic)):
            val.append(vol[___]*m.quote(tic[___]))
        sv = sum(val)
        return sv

def view_hist():
    with Database('TRADER.db') as db:
        q = db.view_his()
        df2 = pd.DataFrame(q)
        
        df2.index += 1
        df2.columns = ['0','Users', 'Buy_Sell', 'Ticker Symbol', 'Price', 'Transaction Volume', 'Money Value']
        df2 = df2.drop(['0'], axis = 1)
        return df2

def view_allpor():
    with Database('TRADER.db') as db:
        qq = db.view_allport()
        df3 = pd.DataFrame(qq)
        df3.index += 1
        df3.columns = ['0','Users', 'Ticker Symbol', 'Owned Volume']
        df3 = df3.drop(columns=['0'])
        return df3

def lookup(company_name):
    return m.lookup(company_name)

def quote(ticker_symbol):
    return m.quote(ticker_symbol)