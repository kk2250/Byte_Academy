import sqlite3


connection = sqlite3.connect('q2-3.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE Users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR
        Username VARCHAR,
        Password VARCHAR,
        Email VARCHAR,
        Phone_num INTEGER
        UNIQUE (Username)
    );
    """
)

cursor.execute(
    """CREATE TABLE Phone_numbers(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Username VARCHAR,
        Phone_num INTEGER
        UNIQUE (Phone_num)
    );
    """
)

cursor.execute(
    """INSERT INTO Users(
        Name,
        Username,
        Password,
        Email
    ) VALUES(
        ?,
        ?,
        ?,
        ?
    );""",(
        'Admin',
        'Admin',
        '1q2w3e4r',
        'byte@byte.com'
    )
)

cursor.execute(
    """INSERT INTO Phone_numbers(
        Username,
        Phone_num
    ) VALUES(
        ?,
        ?
    );""",(
        'Admin',
        1234567890
    )
)

cursor.execute(
    """INSERT INTO Phone_numbers(
        Username,
        Phone_num
    ) VALUES(
        ?,
        ?
    );""",(
        'Admin',
        9876543210
    )
)