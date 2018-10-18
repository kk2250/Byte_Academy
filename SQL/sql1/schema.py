#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('snack.db', check_same_shread=False)
cursor = connection.cursor()

cursor.execute(
	"""CREATE TABLE users(
	pk INTEGER PRIMARY KEY AUTOINCREMENT,
	username VARCHAR(16),
	password VARCHAR(32)
	);"""
)

cursor.close()
connection.close()
