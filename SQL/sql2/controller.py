import sqlite3
import os
import time
import model

while True:
    os.system('clear')
    print('\n\nWhat woud you like to add to our DB?')
    choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n[E]xit')
    if choice.upper() == 'C':
        class_id = input()
        class_room = input()
        number_students = input()
    elif choice.upper() == 'T':
        teacher_id = input()
        teacher_age = input()
        teacher_sub = input()
        pass
    elif choice.upper() == 'S':
        
        
        pass
    elif choice.upper() == 'E':
        print('\n\nExiting.....')
        break
    else:
        print('Invalid choice. Please type C, T, or S')
        time.sleep(3)
    