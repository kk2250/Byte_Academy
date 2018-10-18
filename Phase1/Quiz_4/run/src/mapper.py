import sqlite3

class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name, check_same_thread = False)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def loggin(self, user_id, password):
        self.cursor.execute(
            """SELECT Cur_balance FROM Users
                WHERE User_id = '{User_id}'
                AND Password = '{Password}';
            """.format(
                User_id=user_id,
                Password=password
            )
        )
        current_balance = self.cursor.fetchone()[0]
        return current_balance

    def signup(self, user_id, password):
        self.cursor.execute(
            """INSERT INTO Users(
                User_id,
                Password,
                Cur_balance
            ) VALUES(
                '{User_id}',
                '{Password}',
                {Cur_balance}
            );""".format(
                User_id=user_id,
                Password=password,
                Cur_balance=0
            )
        )