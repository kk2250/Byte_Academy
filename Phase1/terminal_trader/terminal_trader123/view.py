#!/usr/bin/env python3

import os


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
    header()
    print('[b] Buy\n[s] Sell\n[l] Look-up\n[q] Quote\n[e] Exit\n')
    return input('What do you want to do? ')

