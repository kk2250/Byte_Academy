import csv


with open('TSLA.csv', 'r') as file:
    rows = csv.reader(file)
    for row in rows:
        # print(row)
        # print(len(rows))
        print(row[1])