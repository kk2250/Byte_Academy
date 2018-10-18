import time
import os
import pandas as pd
import numpy as np

class Gameboard:
    def __init__(self):
        self.board = ()

    def create_board(self,x):
        self.x = x
        z = np.full((x,x), '#')
        game_board = pd.DataFrame(z)
        game_board.columns += 1
        game_board.index += 1
        return game_board

class Battleship:
    def __init__(self):
        self.ship = ()
        self.missile = ()
        self.number_try = 0


    def place_battleship(self, ):
        while True:
            battleship_x = int(input('PLAYER 1 - Select the row of your battleship:  '))
            battleship_y = int(input('PLAYER 1 - Select the column of your battleship:  '))
        

    # def shoot_missile(self, x, y):

class Missile:
    

    