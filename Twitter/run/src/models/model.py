#!/usr/bin/env python3

from src.mappers.sqlite import Database

database = 'run/src/datastores/master.db'

def sign_up(user_id, password):
    with Database(database) as db:
        db.add_user(user_id,password)

def loggin(user_id,password):
    with Database(database) as db:
        db.log_in(user_id,password)

def user_table(user_id):
    with Database(database) as db:
        db.create_table(user_id)

def user_column(user_id):
    with Database(database) as db:
        db.add_column(user_id,'friend_id','VARCHAR')

def add_tw(user_id,content,time):
    with Database(database) as db:
        db.add_tweet(user_id,content,time)

def find_fri(user_id):
    with Database(database) as db:
        db.find_friend(user_id)

def add_num(user_id,num_tweet):
    with Database(database) as db:
        db.add_num_tweet(user_id,num_tweet)

def find_num_tweet(user_id):
    with Database(database) as db:
        return db.find_num_tweet(user_id)

def suggest_friend():
    with Database(database) as db:
        return db.sug_friend()

def add_friend(user_id,friend_id):
    with Database(database) as db:
        db.add_friend(user_id,friend_id)

def find_all_friend(user_id):
    with Database(database) as db:
        return db.find_all_friend(user_id)

def list_tweets(user_id):
    with Database(database) as db:
        return db.fetch_tweets(user_id)

def fetchall_tweets():
    with Database(database) as db:
        return db.fetchall_tweets()
        
def delete_tweet(user_id,time):
    with Database(database) as db:
        db.delete_tweet(user_id,time)

def delete_tweet1(user_id):
    with Database(database) as db:
        db.delete_tweet1(user_id)

def delete_users(user_id):
    with Database(database) as db:
        db.delete_user1(user_id)
        db.delete_user2(user_id)

def delete_users1(a,b):
    with Database(database) as db:
        db.delete_user3(a,b)