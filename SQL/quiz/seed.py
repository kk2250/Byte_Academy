#!/usr/bin/env python3

import sqlite3
from database import Database

connection = sqlite3.connect('employees.db', check_same_shread=False)
cursor = connection.cursor()

cursor.execute(
	"""INSERT INTO employee(
	name,
	cellphone,
    homephone,
    workphone,
    email,
    country
	) VALUES(
	?,
    ?,
    ?,
    ?,
	?,
    ?
	);""",(
		'spencer',
		'1235',
        '123555',
        '1346634',
        'tracey@aeowrij.com',
        'canada'
        
)

connection.commit()
cursor.close()
connection.close()
