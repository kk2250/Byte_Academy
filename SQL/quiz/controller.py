import sqlite3
import os
import time
import model

while True:
    os.system('clear')
    print('\n\nWhat woud you like to add to our DB?')
    choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n[E]xit\n')
    if choice.upper() == 'C':
        class_id = input()
        class_room = input()
        number_students = input()
    elif choice.upper() == 'T':
        teacher_id = input()
        teacher_name = input()
        teacher_subject = input()
        pass
    elif choice.upper() == 'S':
        student_id = input()
        student_name = input()
        studnet_phone_number = input()
        pass
    elif choice.upper() == 'E':
        print('\n\nExiting.....')
        break
    else:
        print('Invalid choice. Please type C, T, or S')
        time.sleep(3)
    