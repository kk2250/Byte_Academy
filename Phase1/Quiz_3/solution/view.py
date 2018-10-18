import os


def transaction_menu():
    return input('User ID:  '),input('Ticker Symbol:  '), input('Trade Volume:  ')

def lookup_menu():
    return input('Company name:  ')

def quote_menu():
    return input('Ticker Symbol:  ')

def header():
    os.system('clear')
    print('\n*Terminal Trader\n*')
    os.system('cowsay -d "Welcome to Terminal Trader -$(whoami)"')

def main_menu():
    header()
    print('[b] Buy\n[s] Sell\n[l] Look-up\n[q] Quote\n[e] Exit')
    return input('\nWhat')