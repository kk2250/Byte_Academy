import pandas as pd
import numpy as np
import os
import time

def start_game():
    os.system('clear')
    print('Let\'s start BATTLESHIP boardgame!!!!\n')
    time.sleep(1)
    print('We have to make a gameboard first!\n')
    time.sleep(1)

def create_board(x,y):
    z = np.full((x,y), '#')
    game_board = pd.DataFrame(z)
    return game_board

def place_battleship(x,y):
    loc_ship = (x,y)
    return loc_ship

def shoot_missile(x,y):
    loc_mis = (x,y)
    return loc_mis

def missed():
    print('You missed the opponent battleship..')
    time.sleep(2)

def busted():
    print('You sunk the opponent battleship!!!')
    time.sleep(3)


