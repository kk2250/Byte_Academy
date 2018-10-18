import sqlite3

class Database:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self,_type,_value,_traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def create_table(self, _tablename):
        self.cursor.execute(
            """CREATE TABLE {tablename}(
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );
            """.format(
                tablename=_tablename
            )
        )

    def add_column(self,_tablename,_columnname,_columntype):
        self.cursor.execute(
            """ALTER TABLE {tablename}
                ADD COLUMN {columnname} {columntype};
                """.format(
                    tablename=_tablename,
                    columnname=_columnname,
                    columntype=_columntype
                )
            
        )