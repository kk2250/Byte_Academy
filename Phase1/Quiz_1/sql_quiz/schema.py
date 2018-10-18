import csv
from database import Database

with Database('School.db') as db:
    db.create_table('Class')
    db.create_table('Teacher')
    db.create_table('Student')
    # db.ass_column('Class', 'subject')
    # db.ass_column('Class', 'room')
    # db.ass_column('Class', 't_id')
    # db.ass_column('Class', 'capacity')
    # db.ass_column('Class', 'c_id') 
    # db.ass_column('Teacher', 'first')
    # db.ass_column('Teacher', 'last')
    # db.ass_column('Teacher', 'homeroom')
    # db.ass_column('Teacher', 'subj')
    # db.ass_column('Teacher', 'phone')
    # db.ass_column('Teacher', 'tenure')
    # db.ass_column('Teacher', 'age')
    # db.ass_column('Teacher', 'email')
    # db.ass_column('Teacher', 't_id')
    # db.ass_column('Student', 'first')
    # db.ass_column('Student', 'last')
    # db.ass_column('Student', 'gpa')
    # db.ass_column('Student', 'homeroom')
    # db.ass_column('Student', 'year')
    # db.ass_column('Student', 'contact')
    # db.ass_column('Student', 'absences')
    # with open('TSLA.csv', 'r') as file:
    #     rows = csv.reader(file)
    #     for row in rows:
    #         db.add_row(row)