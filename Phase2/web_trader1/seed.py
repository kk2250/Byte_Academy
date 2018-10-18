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
        'admin',
        '1q2w3e4r',
        '0'
    )
)

connection.commit()
cursor.close()
connection.close()