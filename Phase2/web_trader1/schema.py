import sqlite3


connection = sqlite3.connect('TRADER.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE Users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        User_id VARCHAR, 
        Password VARCHAR,
        Current_balance INTEGER,
        UNIQUE(User_id)
    );
    """
)

cursor.execute(
    """CREATE TABLE Trades_history(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        User_id VARCHAR,
        Sell_Buy VARCHAR,
        Ticker_symbol VARCHAR,
        Trade_price FLOAT,
        Trade_volume FLOAT,
        Total FLOAT
    );
    """
)

cursor.execute(
    """CREATE TABLE Portfolio(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        User_id VARCHAR,
        Ticker_symbol VARCHAR,
        Company_volume FLOAT
    );
    """
)

connection.commit()
cursor.close()
connection.close()