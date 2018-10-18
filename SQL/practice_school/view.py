import sqlite3
import os
import time

connection = sqlite3.connect('School.db')
cursor = connection.cursor()

def main_menu():
    print('\n\nWhat woud you like to add to our DB?')
    choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n[L]ookup\n[E]xit')
    return choice

def add_class():
    os.system('clear')
    cursor.execute(
        """.schema Class;"""
    )
    connection.commit()
    cursor.close()
    connection.close()

def success(string):
    connection, cursor = model.connect()
    sql = """SELECT * FROM {};""".format(string)
    cursor.execute(sql)
    result = cursor.fetchall()
    model.disconnect(connection,cursor)
    return result

def add_teacher():
    os.system('clear')
    cursor.execute(
        """.schema Teacher;"""
    )
    connection.commit()
    cursor.close()
    connection.close()

def error():
    print('Your inputs are wrong')

def add_student():
    os.system('clear')
    cursor.execute(
        """.schema Student;"""
    )
    connection.commit()
    cursor.close()
    connection.close()

def lookup():
    os.system('clear')
    print('What table do you want to look at?')
    look_up = input('\n[C]lass\n[T]eacher\n[S]tudent')
    return look_up


