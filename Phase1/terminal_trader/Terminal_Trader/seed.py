import sqlite3

connection = sqlite3.connect('TRADER.db')
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO Users(
        User_id,
        Password,
        Current_balance
    ) VALUES(
        ?,
        ?,
        ?
    );""",(
        'KennyKim',
        'qwert1',
        '10000'
    )
)

connection.commit()
cursor.close()
connection.close()