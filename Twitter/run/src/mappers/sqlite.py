#!/usr/bin/env python3

import sqlite3

class Database:

    def __init__(self,pathname):
        self.connection = sqlite3.connect(pathname,check_same_thread=False)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self,exception_type,exception_value,exception_traceback):
        if self.connection:
            if self.cursor:
                self.cursor.close()
            self.connection.commit()
            self.connection.close()

    def add_admin(self):
        self.cursor.execute(
            '''
            '''
        )

    def create_table(self,tablename):
        self.cursor.execute(
            '''CREATE Table {tablename}(
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );'''.format(
                tablename=tablename
            )
        )

    def add_column(self,_tablename,_columnname,_columntype):
        self.cursor.execute(
            '''ALTER TABLE {tablename}
                ADD COLUMN {columnname} {columntype};'''.format(
                tablename=_tablename,
                columnname=_columnname,
                columntype=_columntype
            )
        )

    def add_user(self,_user_id,_password):
        self.cursor.execute(
            '''INSERT INTO users(
                user_id,
                password,
                num_tweet
                ) VALUES(
                '{user_id}',
                '{password}',
                {num_tweet}
                );'''.format(
                user_id=_user_id,
                password=_password,
                num_tweet=0
            )
        )

    def add_tweet(self,_user_id,_content,_time):
        self.cursor.execute(
            '''INSERT INTO tweet(
                user_id,
                content,
                time) VALUES(
                '{user_id}',
                '{content}',
                '{time}'
                );'''.format(
                user_id=_user_id,
                content=_content,
                time=_time
            )
        )

    def add_friend(self,_user_id,_friend_id):
        self.cursor.execute(
            '''INSERT INTO {user_id}(
                friend_id
                ) VALUES(
                '{friend_id}'
                );'''.format(
                user_id=_user_id,
                friend_id=_friend_id
            )
        )

    def log_in(self,_user_id,_password):
        self.cursor.execute(
            '''SELECT num_tweet FROM users
                WHERE user_id = '{user_id}'
                AND password = '{password}';
            '''.format(
                user_id=_user_id,
                password=_password
            )
        )
        num_tweet = self.cursor.fetchone()[0]
        return num_tweet

    def find_friend(self,_friend):
        self.cursor.execute(
            '''SELECT * FROM {table_name};
            '''.format(
                table_name=_friend
            )
        )

    def add_num_tweet(self,_user_id,_num_tweet):
        self.cursor.execute(
            '''UPDATE users
                SET num_tweet = {num_tweet}
                WHERE user_id = '{user_id}';
            '''.format(
                user_id=_user_id,
                num_tweet=_num_tweet
            )
        )
    
    def find_num_tweet(self,_user_id):
        self.cursor.execute(
            '''SELECT 
            '''
        )

    def find_num_tweet(self,_user_id):
        self.cursor.execute(
            '''SELECT num_tweet FROM users
                WHERE user_id = '{user_id}';
            '''.format(
                user_id=_user_id
            )
        )
        num_tweet = self.cursor.fetchone()[0]
        return num_tweet

    def find_all_friend(self,_user_id):
        self.cursor.execute(
            '''SELECT * From {user_id};
            '''.format(
                user_id=_user_id
            )
        )
        num_friend = self.cursor.fetchall()
        return num_friend

    def sug_friend(self):
        self.cursor.execute(
            '''SELECT user_id FROM users;
            '''
        )
        sug_fri = self.cursor.fetchall()
        return sug_fri
    
    def fetch_tweets(self,_user_id):
        self.cursor.execute(
            '''SELECT * FROM tweet
                WHERE user_id = '{user_id}';
            '''.format(
                user_id=_user_id
            )
        )
        list_tweets = self.cursor.fetchall()
        return list_tweets

    def fetchall_tweets(self):
        self.cursor.execute(
            '''SELECT * FROM tweet;
            '''
        )
        list_tweets = self.cursor.fetchall()
        return list_tweets

    def delete_tweet(self,_user_id,_time):
        self.cursor.execute(
            '''DELETE FROM tweet
                WHERE user_id = '{user_id}'
                AND time = '{time}';
            '''.format(
                user_id=_user_id,
                time=_time
            )
        )

    def delete_tweet1(self,_user_id):
        self.cursor.execute(
            '''DELETE FROM tweet
                WHERE user_id = '{user_id}';
            '''.format(
                user_id=_user_id
            )
        )
    
    def delete_user1(self,_user_id):
        self.cursor.execute(
            '''DROP TABLE {user_id};
            '''.format(
                user_id=_user_id
            )
        )
    
    def delete_user2(self,_user_id):
        self.cursor.execute(
            '''DELETE FROM users
                WHERE user_id = '{user_id}';
            '''.format(
                user_id=_user_id
            )
        )

    def delete_user3(self,tablename,username):
        self.cursor.execute(
            '''DELETE FROM {table}
                WHERE friend_id = '{user_id}';
            '''.format(
                table=tablename,
                user_id=username
            )
        )