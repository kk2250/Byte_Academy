#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('test.db', check_same_shread=False)
cursor = connection.cursor()

cursor.execute(
	"""INSERT INTO users(
	username,
	password
	) VALUES(
	?
	?
	);""",(
		'kennykim',
		'keunchang'
)

connection.commit() # This is kind-of like saving your changes
cursor.close()
connection.close()
