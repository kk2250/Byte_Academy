#!/usr/bin/env python3

from mapper.mapper import Database
from wrapper.wrapper import Markit

m = Markit()

def sign_up(user_id, password):
    with Database('TRADER.db') as db:
        db.signup(user_id,password)

def loggin(user_id,password):
    with Database('TRADER.db') as db:
        return db.loggin(user_id,password)

def lookup(company_name):
    with Markit() as mk:
        return mk.lookup(company_name)

def quote(ticker):
    with Markit() as mk:
        return mk.quote(ticker)

def balance(user_id):
    with Database('TRADER.db') as db:
        return db.check_balance(user_id)

def change_bal(user_id, new_bal):
    with Database('TRADER.db') as db:
        db.change_balance(user_id,new_bal)
        # return db.check_balance(user_id)

def add_buy(user_id, sell_buy, ticker, trade_price, trade_volume, total):
    with Database('TRADER.db') as db:
        return db.add_buy(user_id, sell_buy, ticker, trade_price, trade_volume, total)

def add_sell(user_id, sell_buy, ticker, trade_price, trade_volume, total):
    with Database('TRADER.db') as db:
        return db.add_sell(user_id, sell_buy, ticker, trade_price, trade_volume, total)

def insert_port(user_id, ticker_symbol, company_volume):
    with Database('TRADER.db') as db:
        db.insert_portfolio(user_id, ticker_symbol, company_volume)

def update_port(user_id, ticker_symbol, company_volume):
    with Database('TRADER.db') as db:
        db.update_portfolio(user_id, ticker_symbol, company_volume)

def fetch_all(user_id,ticker_symbol):
    with Database('TRADER.db') as db:
        return db.fetch_all(user_id,ticker_symbol)

def fetch_vol(user_id, ticker_symbol):
    with Database('TRADER.db') as db:
        return db.fetch_volume(user_id, ticker_symbol)

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
        
        # df1 = pd.DataFrame(tot)
        # df1.index +=1
        # df1.columns = ['Ticker symbol', 'Owned Volume', 'Money Value']
        return tot

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
        return q

def view_allpor():
    with Database('TRADER.db') as db:
        qq = db.view_allport()
        return qq

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
        e = []
        for i in range(1,len(a)+1):
            e.append(i)
        c = []
        for ____ in range(len(b)):
            d = [e[____],a[____],b[____]]
            c.append(d)
        d = sorted(c, key=lambda x: x[2], reverse=True)

        return d