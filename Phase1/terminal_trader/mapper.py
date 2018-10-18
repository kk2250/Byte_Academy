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
            """SELECT Current_balance FROM Users
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
                Current_balance
            ) VALUES(
                '{User_id}',
                '{Password}',
                {Current_balance}
            );""".format(
                User_id=user_id,
                Password=password,
                Current_balance=10000.
            )
        )
    
    def check_balance(self, user_id):
        self.cursor.execute(
            """SELECT Current_balance 
                FROM Users
                WHERE User_id = '{User_id}';
            """.format(
                User_id=user_id
            )
        )
        new_balance = self.cursor.fetchone()[0]
        return new_balance

    def add_buy(self, user_id,sell_buy, ticker_symbol,trade_price,trade_volume,total):
        self.cursor.execute(
            """INSERT INTO Trades_history(
                User_id,
                Sell_Buy,
                Ticker_symbol,
                Trade_price,
                Trade_volume,
                Total
            ) VALUES(
                '{User_id}',
                '{Sell_Buy}',
                '{Ticker_symbol}',
                {Trade_price},
                {Trade_volume},
                {Total}
            );""".format(
                User_id=user_id,
                Sell_Buy=sell_buy,
                Ticker_symbol=ticker_symbol,
                Trade_price=trade_price,
                Trade_volume=trade_volume,
                Total=total
            )
        )


    def add_sell(self, user_id,sell_buy, ticker_symbol,trade_price,trade_volume,total):
        self.cursor.execute(
            """INSERT INTO Trades_history(
                User_id,
                Sell_Buy,
                Ticker_symbol,
                Trade_price,
                Trade_volume,
                Total
            ) VALUES(
                '{User_id}',
                '{Sell_Buy}',
                '{Ticker_symbol}',
                {Trade_price},
                {Trade_volume},
                {Total}
            );""".format(
                User_id=user_id,
                Sell_Buy=sell_buy,
                Ticker_symbol=ticker_symbol,
                Trade_price=trade_price,
                Trade_volume=trade_volume,
                Total=total
            )
        )

    def change_balance(self,user_id,new_balance):
        self.cursor.execute(
            """UPDATE Users
                SET Current_balance = {Current_balance}
                WHERE User_id = '{User_id}';
            """.format(
                User_id=user_id,
                Current_balance = new_balance
            )
        )

    def fetch_volume(self, user_id, ticker_symbol):
        self.cursor.execute(
            """SELECT Company_volume FROM Portfolio
                WHERE User_id = '{User_id}'
                AND Ticker_symbol = '{Ticker_symbol}';
            """.format(
                User_id=user_id,
                Ticker_symbol=ticker_symbol
            )
        )
        c_volume = self.cursor.fetchone()[0]
        return c_volume

    def insert_portfolio(self, user_id, ticker_symbol, company_volume):
        self.cursor.execute(
            """INSERT INTO Portfolio(
                User_id,
                Ticker_symbol,
                Company_volume
            ) VALUES(
                '{User_id}',
                '{Ticker_symbol}',
                {Company_volume}
            );
            """.format(
                User_id=user_id,
                Ticker_symbol=ticker_symbol,
                Company_volume=company_volume
            )
        )

    def update_portfolio(self, user_id, ticker_symbol, company_volume):
        self.cursor.execute(
            """UPDATE Portfolio
                SET Company_volume = {Company_volume}
                WHERE User_id = '{User_id}'
                AND Ticker_symbol = '{Ticker_symbol}';
            """.format(
                Company_volume=company_volume,
                User_id=user_id,
                Ticker_symbol=ticker_symbol
            )
        )
    
    def fetch_all(self,user_id,ticker_symbol):
        self.cursor.execute(
            """SELECT * FROM Portfolio
                WHERE User_id = '{User_id}'
                AND Ticker_symbol = '{Ticker_symbol}';
            """.format(
                User_id=user_id,
                Ticker_symbol=ticker_symbol
            )
        )
        return self.cursor.fetchone()[0]

    def list_volume(self, user_id):
        self.cursor.execute(
            """SELECT * FROM Portfolio
                WHERE User_id = '{User_id}';
            """.format(
                User_id=user_id
            )
        )
        return self.cursor.fetchall()

    def fetch_alluser(self):
        self.cursor.execute(
            """SELECT User_id FROM Portfolio;
            """
        )
        return self.cursor.fetchall()

    def view_his(self):
        self.cursor.execute(
            """SELECT * FROM Trades_history;
            """
        )
        return self.cursor.fetchall()

    def view_allport(self):
        self.cursor.execute(
            """SELECT * FROM Portfolio;
            """
        )
        return self.cursor.fetchall()