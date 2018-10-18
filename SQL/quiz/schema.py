from database import Database

with Database('employees.db') as db:
    db.create_table('employee')
    db.ass_column('employee', 'name')
    db.ass_column('employee', 'cellphone')
    db.ass_column('employee', 'homephone')
    db.ass_column('employee', 'workphone')
    db.ass_column('employee', 'email')
    db.ass_column('employee', 'country')