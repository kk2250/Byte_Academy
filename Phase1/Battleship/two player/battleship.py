import view
import pandas as pd
import time
import os
import sys

view.start_game()
board_x = int(input('How many rows should board be?  '))
board_y = int(input('How many columns should board be?  '))
game_board = view.create_board(board_x,board_y)
print(game_board)
time.sleep(1)
while True:
    os.system('clear')
    print(game_board)
    battleship_x = int(input('Select the row of your battleship:  '))
    battleship_y = int(input('Select the column of your battleship:  '))
    if (0 <= battleship_x < board_x) and (0 <= battleship_y < board_y):
        break
    else:
        print('You placed battleship outside the board.')
        time.sleep()
        print('Please re-enter the coordinate of battleship.')



location_battleship = view.place_battleship(battleship_x,battleship_y)

while True:
    os.system('clear')
    print(game_board)
    missile_x = int(input('Select the row of your missile:  '))
    missile_y = int(input('Select the column of your missile:  '))
    location_missile = view.shoot_missile(missile_x,missile_y)
    if game_board.iloc[location_missile] == 'O':
        print('You already shot on the same spot before, try again')
        time.sleep(2)
    elif location_battleship == location_missile:
        game_board.iloc[location_missile] = 'X'
        os.system('clear')
        print(game_board)
        view.busted()
        os.system('clear')
        break
    elif (0 <= missile_x < board_x) and (0 <= missile_y < board_y):
        game_board.iloc[location_missile] = 'O'
        print(game_board)
        view.missed()
    else:
        print('Your missile is out of range, please shoot the missile within the board!!')
        time.sleep(2)



