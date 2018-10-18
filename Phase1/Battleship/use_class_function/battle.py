from class1 import Gameboard as gb
from class1 import Battleship as bp
import time
import os

os.system('clear')
player1_board = gb()
# player2_board = gb()
player1_ship = bp()
# player2_ship = bp()
board_size = int(input('\nWhat is the size of the board?  '))
os.system('clear')
board_1 = player1_board.create_board(board_size)
print(board_1,'\n')
# board_2 = player2_board.create_board(board_size)
# print(board_2,'\n')
while True:
    player1_battleship_x = int(input('PLAYER 1 - Select the row of your battleship:  '))
    player1_battleship_y = int(input('PLAYER 1 - Select the column of your battleship:  '))
    if (1 <= player1_battleship_x <= board_size) and (1 <= player1_battleship_y <= board_size):
        player1_ship.ship = (player1_battleship_x,player1_battleship_y)
        break
    else:
        print('Your battleship is out of the board, try again.')
# while True:
#     player2_battleship_x = int(input('PLAYER 2 - Select the row of your battleship:  '))
#     player2_battleship_y = int(input('PLAYER 2 - Select the column of your battleship:  '))
#     if (1 <= player2_battleship_x <= board_size) and (1 <= player2_battleship_y <= board_size):
#         player2_ship.ship = (player2_battleship_x,player2_battleship_y)
#         break
#     else:
#         print('Your battleship is out of the board, try again.')

while True:
    os.system('clear')
    print(board_1,'\n')
    # print(board_2,'\n')

    player1_missile_x = int(input('PLAYER 1 - Select the row of your missile:  '))
    player1_missile_y = int(input('PLAYER 1 - Select the column of your missile:  '))
    player1.missile = (player1_missile_x,player1_missile_y)

    # player2_missile_x = int(input('PLAYER 2 - Select the row of your missile:  '))
    # player2_missile_y = int(input('PLAYER 2 - Select the column of your missile:  '))
    # player2.missile = (player2_missile_x,player2_missile_y)
