import sqlite3
from sqlite import Database

with Database('run/src/datastores/master.db') as database:
    database.create_table('tweet')
    # database.create_table('user_id')
    database.create_table('users')
    database.add_column('tweet','user_id','VARCHAR')
    database.add_column('tweet','content','BLOB')
    database.add_column('tweet','time','VARCHAR')
    # database.add_column('user_id','friend_id','VARCHAR')
    database.add_column('users','user_id','VARCHAR')
    database.add_column('users','password','VARCHAR')
    database.add_column('users','num_tweet','INTEGER')
    # database.add_tweet('users','num_tweet','INTEGER')
