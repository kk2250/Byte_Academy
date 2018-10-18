import sqlite3
import os
import time

from model import Database as db
import view
 
while True:
    choice = view.main_menu()
    # print('\n\nWhat woud you like to add to our DB?')
    # choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n[E]xit')
    if choice.upper() == 'C':
        view.add_class()
        subject = input('Subject: ')
        room = int(input('Room number: '))
        t_id = int(input('Teacher ID: '))
        capacity = int(input('Class capaciiy: '))
        c_id = int(input('Class ID: '))
        success = db.add_class(subject,room,t_id,capacity,c_id)
        if success:
            view.success('Class')
        else:
            view.error()

    elif choice.upper() == 'T':
        view.add_teacher()
        first = input('First name: ')
        last = input('Last name: ')
        homeroom = int(input('Homeroom number: '))
        subj = input('Subject: ')
        phone = input('Phone number: ')
        age = int(input('Age: '))
        email = input('Email: ')
        success = db.add_teacher(first,last,homeroom,subj,phone,
                                    age,email)
        if success:
            view.success('Teacher')
        else:
            view.error()

    elif choice.upper() == 'S':
        view.add_student()
        first = input('First name: ')
        last = input('Last name: ')
        gpa = float(input('GPA: '))
        homeroom = int(input('Homeroom number: '))
        year = int(input('Year: '))
        contact = str(input('Emergency phone number: '))
        success = db.add_student(first,last,gpa,homeroom,
                                    year,contact)
        if success:
            view.success('student')
        else:
            view.error()

    elif choice.upper() == 'L':
        lookup_choice = view.lookup()
        if lookup_choice == 'S':
            result = db.lookup_all('students')
        elif lookup_choice == 'C':
            result = db.lookup_all('classes')
        elif lookup_choice == 'T':
            result = db.lookup_all('teachers')
        else:
            print('Error, please choose C, T, S.')
            time.sleep(3)
        print(result)
        time.sleep(5)

    elif choice.upper() == 'E':
        print('\n\nExiting.....')
        time.sleep(2)
        os.system('clear')
        #TODO make this view.exit()
        break



"""
def model.lookup_all(table_name):
    connection, cursor = model.connect()
    sql = \"""SELECT * FROM {};\""".format(table_name)
    cursor.execute(sql)
    result = cursor.fetchall()
    model.disconnect(connection,cursor)
    return result
"""