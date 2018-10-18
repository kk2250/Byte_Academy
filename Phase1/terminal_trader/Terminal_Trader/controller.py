#!/usr/bin/env python3

import model
import view
import os
import time
import sqlite3

view.header()
player = view.player()
if player.upper() == 'Y':
    while True:
        try:
            (user_id, password) = view.new_player()
            model.sign_up(user_id,password)
            break
        except sqlite3.IntegrityError:
            print('User_ID is already exist.')
else:
    while True:
        try:
            (user_id, password) = view.log_in()
            model.login(user_id, password)
            break
        except TypeError:
            print('Wrong User_ID or Password.')
            time.sleep(1)


while True:
    buy_inputs = ['b','buy']
    sell_inputs = ['s','sell']
    lookup_inputs = ['l','lookup','look up','look-up']
    quote_inputs = ['q','quote']
    exit_inputs = ['e','exit','quit']
    acceptable_inputs = buy_inputs     \
                        +sell_inputs   \
                        +lookup_inputs \
                        +quote_inputs  \
                        +exit_inputs

    os.system('clear')
    view.header()
    print('\nYour current balance is:', end=' ')
    print(model.check_balance(user_id))
    print(' ')
    user_input = view.main_menu()

    if user_input in acceptable_inputs:
        if user_input in buy_inputs:
            (ticker_symbol,trade_volume) = view.transaction_menu()
            model.buy(user_id, ticker_symbol,trade_volume)
            time.sleep(2)
        elif user_input in sell_inputs:
            (ticker_symbol,trade_volume) = view.transaction_menu()
            model.sell(user_id, ticker_symbol,trade_volume)
            time.sleep(2)
        elif user_input in lookup_inputs:
            print(model.lookup(view.lookup_menu()))
            time.sleep(1)
        elif user_input in quote_inputs:
            print(model.quote(view.quote_menu()))
            time.sleep(1)
        elif user_input in exit_inputs:
            break