import os
import time

def main_menu():
    print('\nDo you want to play Monty Hall game?')
    choice = input('Press [Y]es if you want to play, press [N]o if you don\'t want to play: \n  ')
    return choice

def choose_door():
    os.system('clear')
    print('\nThere are three doors in front of you')
    time.sleep(1)
    print('Behind one of the doors is a brand new car. Behind the other two are goats.')
    time.sleep(2)
    print('Choose one of three doors')
    time.sleep(1)

def prize(answer):
    if answer.lower() == 'y':
        os.system('clear')
        print('You decided to switch! COOL!')
        time.sleep(2)
    elif answer.lower() == 'n':
        os.system('clear')
        print('You decided not to switch! COOL!')
        time.sleep(2)
