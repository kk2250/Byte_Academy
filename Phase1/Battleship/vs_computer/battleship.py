import view
import pandas as pd
import time
import os
import sys

view.start_game()

board_x = int(input('How many rows should board be?  '))
board_y = int(input('How many columns should board be?  '))

game_board = view.create_board(board_x,board_y)
while True:
    print(game_board)
    battleship_x = int(input('Select the row of your battleship:  '))
    battleship_y = int(input('Select the column of your battleship:  '))
    if (0 < battleship_x < board_x) and (0 < battleship_y < board_y):
        break
    else:
        print('You placed battleship outside the board.')
        print('Please re-enter the coordinate of battleship.')



location_battleship = view.place_battleship(battleship_x,battleship_y)

while True:
        print(game_board)
        missile_x = int(input('Select the row of your missile:  '))
        missile_y = int(input('Select the column of your missile:  '))
        location_missile = view.shoot_missile(missile_x,missile_y)
        if location_battleship == location_missile:
            game_board.iloc[location_missile] = 'X'
            print(game_board)
            view.busted()
            break
        else:
            game_board.iloc[location_missile] = 'O'
            print(game_board)
            view.missed()



