import sqlite3


connection = sqlite3.connect('Login.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE Users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        User_id VARCHAR, 
        Password VARCHAR,
        Cur_balance INTEGER,
        UNIQUE(User_id)
    );
    """
)

connection.commit()
cursor.close()
connection.close()