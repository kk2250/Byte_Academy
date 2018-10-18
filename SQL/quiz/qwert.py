import csv

with open('employees.csv', 'r') as file:
    rows = csv.reader(file)
    for row in rows:
        print(row)
