import sqlite3


connection = sqlite3.connect('School.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE Class(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
	subject VARCHAR,
    room INTEGER,
    t_id INTEGER,
    capacity INTEGER,
    c_id INTEGER
    );"""
)

cursor.execute(
    """CREATE TABLE Teacher(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
	first VARCHAR,
    last VARCHAR,
    homeroom INTEGER,
    subj VARCHAR,
    phone INTEGER,
    age INTEGER,
    email VARCHAR
    );"""
)

cursor.execute(
    """CREATE TABLE Student(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
	first VARCHAR,
    last VARCHAR,
    gpa FLOAT,
    homeroom INTEGER,
    year INTEGER,
    contact INTEGER
    );"""
)

connection.commit()
connection.close()