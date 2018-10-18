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

if user_id == 'Admin':
    while True:
        lookup_inputs = ['l','lookup','look up','look-up']
        quote_inputs = ['q','quote']
        view_history_inputs = ['vh', 'v', 'history']
        view_all_portfolio_inputs = ['vp', 'portfolio']
        leaderboard_inputs = ['lb', 'leaderboard']
        exit_inputs = ['e','exit','quit']
        acceptable_inputs = lookup_inputs \
                            +quote_inputs  \
                            +view_history_inputs \
                            +view_all_portfolio_inputs \
                            +leaderboard_inputs   \
                            +exit_inputs
        os.system('clear')
        view.header()
        print(' ')
        user_input = view.main_menu1()

        if user_input in acceptable_inputs:
            if user_input in lookup_inputs:
                print(model.lookup(view.lookup_menu()))
                time.sleep(1)
            elif user_input in quote_inputs:
                print(model.quote(view.quote_menu()))
                time.sleep(1)
            elif user_input in view_history_inputs:
                os.system('clear')
                print(model.view_hist())
                input('\nDo you want to exit the leaderboard? [Y]  '  )
            elif user_input in view_all_portfolio_inputs:
                os.system('clear')
                print(model.view_allpor())
                input('\nDo you want to exit the leaderboard? [Y]  '  )
            elif user_input in leaderboard_inputs:
                os.system('clear')
                print(model.leaderboard())
                input('\nDo you want to exit the leaderboard? [Y]  '  )
            elif user_input in exit_inputs:
                break

else:
    while True:
        buy_inputs = ['b','buy']
        sell_inputs = ['s','sell']
        view_port_inputs = ['v', 'view', 'portfolio']
        lookup_inputs = ['l','lookup','look up','look-up']
        quote_inputs = ['q','quote']
        exit_inputs = ['e','exit','quit']
        acceptable_inputs = buy_inputs     \
                            +sell_inputs   \
                            +view_port_inputs  \
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
            elif user_input in view_port_inputs:
                os.system('clear')
                print(model.view_port(user_id))
                print('\nYour current balance is:', end=' ')
                print(model.check_balance(user_id))
                print('\nYour total balance is:  ', model.sum_val(user_id)+model.check_balance(user_id))
                input('\nDo you want to exit portfolio? [Y]  ')
            elif user_input in lookup_inputs:
                print(model.lookup(view.lookup_menu()))
                time.sleep(1)
            elif user_input in quote_inputs:
                print(model.quote(view.quote_menu()))
                time.sleep(1)
            elif user_input in exit_inputs:
                break