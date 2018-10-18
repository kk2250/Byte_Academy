#!/usr/bin/env python3

import os


def player():
    return input('Are you a new user?[Y/N]  ')

def new_player():
    return input('Enter New User ID:  '), input('Enter New Password:  ')

def log_in():
    return input('User ID:  '),input('Password:  ')

def transaction_menu():
    return input('Ticker Symbol: '),input('Trade Volume: ')

def lookup_menu():
    return input('Company name: ')

def quote_menu():
    return input('Ticker Symbol: ')

def header():
    os.system('clear')
    print('\n* Terminal Trader *\n')
    os.system('cowsay -s "Welcome to Terminal Trader -$(whoami)"')

def main_menu():
    print('[b] Buy\n[s] Sell\n[v] View Portfolio \n[l] Look-up\n[q] Quote\n[e] Exit\n')
    return input('What do you want to do? ')

def main_menu1():
    print('[l] Look-up\n[q] Quote\n[vh] View History\n[vp] View Portfolio\n[lb] Leaderboard \n[e] Exit\n')
    return input('What do you want to do? ')
