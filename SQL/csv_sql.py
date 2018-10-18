import sqlite3
import csv

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (name, cellphone, homephone, workphone, email, country);") # use your column names here

with open('employees.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['name'], i['cellphone'], i['homephone'], i['workphone'], i['email'], i['country']) for i in dr]

cur.executemany("INSERT INTO t (name, cellphone, homephone, workphone, email, country) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()