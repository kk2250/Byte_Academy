import view
import pandas as pd
import time
import os
import sys

view.start_game()
board_x = int(input('How many rows should board be?  '))
board_y = int(input('How many columns should board be?  '))
game_board_1 = view.create_board(board_x,board_y)
game_board_2 = view.create_board(board_x,board_y)
os.system('clear')
print('PLAYER 1')
print(game_board_1, '\n')
print('PLAYER 2')
print(game_board_2, '\n')
time.sleep(2)

while True:
    os.system('clear')
    print('PLAYER 1')
    print(game_board_1, '\n')
    print('PLAYER 2')
    print(game_board_2, '\n')
    battleship_x_1 = int(input('PLAYER 1 - Select the row of your battleship:  '))
    battleship_y_1 = int(input('PLAYER 1 - Select the column of your battleship:  '))
    if (0 <= battleship_x_1 < board_x) and (0 <= battleship_y_1 < board_y):
        print('Battleship location for PLAYER 1 : (' + str(battleship_x_1) + ', ' + str(battleship_y_1) + ')')
        time.sleep(2)
        break
    else:
        print('You placed battleship outside the board.')
        time.sleep(2)
        print('Please re-enter the coordinate of battleship.')
        time.sleep(2)



while True:
    os.system('clear')
    print('PLAYER 1')
    print(game_board_1, '\n')
    print('PLAYER 2')
    print(game_board_2, '\n')
    battleship_x_2 = int(input('PLAYER 2 - Select the row of your battleship:  '))
    battleship_y_2 = int(input('PLAYER 2 - Select the column of your battleship:  '))
    if (0 <= battleship_x_2 < board_x) and (0 <= battleship_y_2 < board_y):
        print('Battleship location for PLAYER 2 : (' + str(battleship_x_2) + ', ' + str(battleship_y_2) + ')')
        time.sleep(2)
        break
    else:
        print('You placed battleship outside the board.')
        time.sleep(2)
        print('Please re-enter the coordinate of battleship.')
        time.sleep(2)

location_battleship_1 = view.place_battleship(battleship_x_1,battleship_y_1)
location_battleship_2 = view.place_battleship(battleship_x_2,battleship_y_2)
os.system('clear')
print('Great!\n')
time.sleep(1)
print('Let\'s play the game now!')
time.sleep(2)

while True:
    os.system('clear')
    while True:
        os.system('clear')
        print('PLAYER 1')
        print(game_board_1, '\n')
        print('PLAYER 2')
        print(game_board_2, '\n')
        missile_x_1 = int(input('PLAYER 1 - Select the row of your missile:  '))
        missile_y_1 = int(input('PLAYER 1 - Select the column of your missile:  '))
        os.system('clear')
        location_missile_1 = view.shoot_missile(missile_x_1,missile_y_1)
        if game_board_2.iloc[location_missile_1] == 'O':
            print('You already shot on the same spot before, try again')
            time.sleep(2)
        elif location_battleship_2 == location_missile_1:
            game_board_2.iloc[location_missile_1] = 'X'
            print('PLAYER 1')
            print(game_board_1, '\n')
            print('PLAYER 2')
            print(game_board_2, '\n')
            time.sleep(2)
            view.busted()
            os.system('clear')
            print('Now! PLAYER 2 has one last chance to sink PLAYER 1 battleship.')
            time.sleep(3)
            break
        elif (0 <= missile_x_1 < board_x) and (0 <= missile_y_1 < board_y):
            game_board_2.iloc[location_missile_1] = 'O'
            print('PLAYER 1')
            print(game_board_1, '\n')
            print('PLAYER 2')
            print(game_board_2, '\n')
            time.sleep(1)
            view.missed()
            break
        else:
            print('Your missile is out of range, please shoot the missile within the board!!')
            time.sleep(2)

    while True:
        os.system('clear')
        print('PLAYER 1')
        print(game_board_1, '\n')
        print('PLAYER 2')
        print(game_board_2, '\n')
        missile_x_2 = int(input('PLAYER 2 - Select the row of your missile:  '))
        missile_y_2 = int(input('PLAYER 2 - Select the column of your missile:  '))
        location_missile_2 = view.shoot_missile(missile_x_2,missile_y_2)
        if game_board_1.iloc[location_missile_2] == 'O':
            print('You already shot on the same spot before, try again')
            time.sleep(2)
        elif location_battleship_1 == location_missile_2:
            game_board_1.iloc[location_missile_2] = 'X'
            print('PLAYER 1')
            print(game_board_1, '\n')
            print('PLAYER 2')
            print(game_board_2, '\n')
            time.sleep(2)
            view.busted()
            break
        elif (0 <= missile_x_2 < board_x) and (0 <= missile_y_2 < board_y):
            game_board_1.iloc[location_missile_2] = 'O'
            print('PLAYER 1')
            print(game_board_1, '\n')
            print('PLAYER 2')
            print(game_board_2, '\n')
            time.sleep(1)
            view.missed()
            break
        else:
            print('Your missile is out of range, please shoot the missile within the board!!')
    if (location_battleship_2 == location_missile_1):
        os.system('clear')
        print('\nPLAYER 1 is WINNER!!!')
        os.system('clear')
        time.sleep(2)
        break
    elif (location_battleship_1 == location_missile_2):
        os.system('clear')
        print('\nPLAYER 2 is WINNER!!!')
        time.sleep(2)
        os.system('clear')
        break
    else:
        pass