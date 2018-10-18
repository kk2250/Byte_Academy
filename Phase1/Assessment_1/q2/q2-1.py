import sqlite3


connection = sqlite3.connect('q2-1.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE Cities(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        State VARCHAR,
        City VARCHAR
    );
    """
)

cursor.execute(
    """CREATE TABLE Parks(
        ph INTEGER PRIMARY KEY AUTOINCREMENT,
        State VARCHAR,
        Park VARCHAR
    );
    """
)