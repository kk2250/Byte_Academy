#!/usr/bin/env python3

from database_access_object import Database

with Database('themas.db') as db:
    # db.create_table('students')
    db.ass_column('students', 'nickname')