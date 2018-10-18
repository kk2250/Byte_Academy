#!/usr/bin/env python3

import sqlite3
import csv


connection = sqlite3.connect('TSLA.db', check_same_shread=False)
cursor = connection.cursor()

with open('TSLA.csv', 'r') as file:
    rows = csv.reader(file)
    for row in rows:
        cursor.execute(
            """INSERT INTO TSLA_MARKET_DATA(
            Open,
            High,
            Low,
            Close,
            Adj Close,
            Volume
            ) VALUES(
            ?,?,?,?,?,?
            );""",(
                str(row[0]),
                str(row[1]),
                str(row[2]),
                str(row[3]),
                str(row[4]),
                str(row[5])   
        )
        connection.commit()
        cursor.close()
        connection.close()
