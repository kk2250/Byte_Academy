import sqlite3
import os
import time
import modelll

while True:
    os.system('clear')  # hit clear every loop
    print('\n\nWhat would you like to add to our DB?')
    choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n')
    if choice.upper() == 'C':
        pass
    elif choice.upper() == 'T':
        pass
    elif choice.upper() == 'S':
        pass
    elif choice.upper() == 'E':
        print('\n\nExiting.....')
        break
    else:
        print('Invalid choice, Please type  C, T, or S')
        time.sleep(3)  #wait for 3 seconds