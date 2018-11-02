#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for
import src.models.model as model
import sqlite3
import datetime as dt


controller = Blueprint('public',__name__)

@controller.route('/',methods=['GET','POST'])
def globall():
    if request.method == 'GET':
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        return render_template('unauthorized/global.html', list_of_tweets=list_of_tweets)

@controller.route('/login',methods=['GET','POST'])
def log_in():
    if request.method == 'GET':
        return render_template('unauthorized/login.html')
    elif request.method == 'POST':
        session['user_id'] = request.form['user_id']
        password = request.form['password']
        if session['user_id'] and password:
            if session['user_id'] == 'admin' and password == '1q2w3e4r':
                return redirect('/admin')
            try:
                model.loggin(session['user_id'], password)
                return redirect('/newsfeed')
            except TypeError:
                message = 'Invalid username or password.'
                return render_template('unauthorized/login.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('unauthorized/login.html', message=message)

@controller.route('/login_new',methods=['GET','POST'])
def log_in_new():
    if request.method == 'GET':
        return render_template('unauthorized/login_new.html')
    elif request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id and password:
            try:
                model.sign_up(user_id, password)
                model.user_table(user_id)
                model.user_column(user_id)
                return redirect('/login')
            except sqlite3.OperationalError:
                message = 'Username is already exist.'
                return render_template('unauthorized/login_new.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('unauthorized/login_new.html', message=message)

@controller.route('/newsfeed',methods=['GET','POST'])
def newsfeed():
    if request.method == 'GET':
        User_ID=session['user_id']
        num_tweet = model.find_num_tweet(session['user_id'])
        num_friend = len(model.find_all_friend(session['user_id']))
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            list_of_friend = []
            qq = model.find_all_friend(session['user_id'])
            for __ in qq:
                list_of_friend.append(__[1])
            if _[1] in list_of_friend:
                q = [_[1],_[2],_[3]]
                list_of_tweets.insert(0, q)
            elif _[1] == session['user_id']:
                q = [_[1],_[2],_[3]]
                list_of_tweets.insert(0, q)
        return render_template('authorized/newsfeed.html', num_tweet=num_tweet, num_friend=num_friend, list_of_tweets=list_of_tweets, User_ID=User_ID)
    elif request.method == 'POST':
        Content = request.form['content']
        if Content:
            t = str(dt.datetime.now())
            time_now = t[:19]
            num_tweet = model.find_num_tweet(session['user_id']) + 1
            model.add_tw(session['user_id'],Content,time_now)
            model.add_num(session['user_id'],num_tweet)
            num_friend = len(model.find_all_friend(session['user_id']))
            tweets = model.fetchall_tweets()
            list_of_tweets = []
            for _ in tweets:
                list_of_friend = []
                qq = model.find_all_friend(session['user_id'])
                for __ in qq:
                    list_of_friend.append(__[1])
                if _[1] in list_of_friend:
                    q = [_[1],_[2],_[3]]
                    list_of_tweets.insert(0, q)
                elif _[1] == session['user_id']:
                    q = [_[1],_[2],_[3]]
                    list_of_tweets.insert(0, q)
            return render_template('authorized/newsfeed.html', num_tweet=num_tweet, num_friend=num_friend, list_of_tweets=list_of_tweets, User_ID=session['user_id'])

@controller.route('/account',methods=['GET','POST'])
def account():
    if request.method == 'GET':
        Username = session['friend_id']
        friends = model.find_all_friend(session['friend_id'])
        list_of_friends = []
        for __ in friends:
            list_of_friends.append(__[1])
        tweets = model.list_tweets(session['friend_id'])
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        if session['friend_id']:
            if session['friend_id'] == session['user_id']:
                num_tweet = model.find_num_tweet(session['user_id'])
                num_friend = len(model.find_all_friend(session['user_id']))
                friends = model.find_all_friend(session['user_id'])
                list_of_friends = []
                for __ in friends:
                    list_of_friends.append(__[1])
                tweets = model.list_tweets(session['user_id'])
                list_of_tweets = []
                for _ in tweets:
                    q = [_[1],_[2],_[3]]
                    list_of_tweets.insert(0, q)
                return render_template('authorized/me.html', list_of_tweets=list_of_tweets, list_of_friends=list_of_friends, num_tweet=num_tweet, num_friend=num_friend, username=session['user_id'])
            try:
                model.find_fri(session['friend_id'])
                num_tweet = model.find_num_tweet(session['friend_id'])
                num_friend = len(model.find_all_friend(session['friend_id']))
                return render_template('authorized/account.html', list_of_friends=list_of_friends, list_of_tweets=list_of_tweets, num_tweet=num_tweet, num_friend=num_friend, username=session['friend_id'], msg=session['friend_id'])
            except sqlite3.OperationalError:
                a = model.suggest_friend()
                b = []
                c = []
                y = model.find_all_friend(session['user_id'])
                for _ in y:
                    c.append(y[0][1])
                for x in a:
                    if session['user_id'] != x[0]:
                        if x[0] not in c:
                            num_tweet = model.find_num_tweet(x[0])
                            num_friend = len(model.find_all_friend(x[0]))
                            alllist = [x[0],num_tweet,num_friend]
                            b.append(alllist)
                message = 'There is no Supremer called ' + Username + '.'
                return render_template('authorized/suggestion.html', message=message, suggestions=b)
    elif request.method == 'POST':
        session['friend_id'] = request.form['username']
        Username = session['friend_id']
        friends = model.find_all_friend(session['friend_id'])
        list_of_friends = []
        for __ in friends:
            list_of_friends.append(__[1])
        tweets = model.list_tweets(session['friend_id'])
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        if session['friend_id']:
            if session['friend_id'] == session['user_id']:
                num_tweet = model.find_num_tweet(session['user_id'])
                num_friend = len(model.find_all_friend(session['user_id']))
                friends = model.find_all_friend(session['user_id'])
                list_of_friends = []
                for __ in friends:
                    list_of_friends.append(__[1])
                tweets = model.list_tweets(session['user_id'])
                list_of_tweets = []
                for _ in tweets:
                    q = [_[1],_[2],_[3]]
                    list_of_tweets.insert(0, q)
                return render_template('authorized/me.html', list_of_tweets=list_of_tweets, list_of_friends=list_of_friends, num_tweet=num_tweet, num_friend=num_friend, username=session['user_id'])
            try:
                model.find_fri(session['friend_id'])
                num_tweet = model.find_num_tweet(session['friend_id'])
                num_friend = len(model.find_all_friend(session['friend_id']))
                return render_template('authorized/account.html', list_of_friends=list_of_friends, list_of_tweets=list_of_tweets, num_tweet=num_tweet, num_friend=num_friend, username=session['friend_id'], msg=session['friend_id'])
            except sqlite3.OperationalError:
                a = model.suggest_friend()
                b = []
                c = []
                y = model.find_all_friend(session['user_id'])
                for _ in y:
                    c.append(y[0][1])
                for x in a:
                    if session['user_id'] != x[0]:
                        if x[0] not in c:
                            num_tweet = model.find_num_tweet(x[0])
                            num_friend = len(model.find_all_friend(x[0]))
                            alllist = [x[0],num_tweet,num_friend]
                            b.append(alllist)
                message = 'There is no Supremer called ' + Username + '.'
                return render_template('authorized/suggestion.html', message=message, suggestions=b)

@controller.route('/suggestion',methods=['GET','POST'])
def suggestion():
    if request.method == 'GET':
        a = model.suggest_friend()
        b = []
        c = []
        y = model.find_all_friend(session['user_id'])
        for _ in y:
            c.append(_[1])
        for x in a:
            if session['user_id'] != x[0]:
                if x[0] not in c:
                    num_tweet = model.find_num_tweet(x[0])
                    num_friend = len(model.find_all_friend(x[0]))
                    alllist = [x[0],num_tweet,num_friend]
                    b.append(alllist)
        return render_template('authorized/suggestion.html', suggestions=b)
    elif request.method == 'POST':
        session['friend'] = request.form['go']
        friends = model.find_all_friend(session['friend'])
        list_of_friends = []
        for __ in friends:
            list_of_friends.append(__[1])
        tweets = model.list_tweets(session['friend'])
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        num_tweet = model.find_num_tweet(session['friend'])
        num_friend = len(model.find_all_friend(session['friend']))
        return render_template('authorized/account.html', list_of_friends=list_of_friends, list_of_tweets=list_of_tweets, num_tweet=num_tweet, num_friend=num_friend, username=session['friend'], msg=session['friend'])

@controller.route('/follow',methods=['GET','POST'])
def follow():
    if request.method == 'GET':
        tweets = model.list_tweets(session['friend_id'])
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        return render_template('authorized/account.html', list_of_tweets=list_of_tweets, username=session['friend_id'], msg=session['friend_id'])
    elif request.method == 'POST':
        y = request.form['follow']
        if session['friend']:
            num_tweet = model.find_num_tweet(session['friend'])
            num_friend = len(model.find_all_friend(session['friend']))
            x = model.find_all_friend(session['user_id'])
            for _ in range(len(x)):
                if x[_][1] == y:
                    message = 'You already followed ' + y + '.'
                    tweets = model.list_tweets(session['friend'])
                    list_of_tweets = []
                    for _ in tweets:
                        q = [_[1],_[2],_[3]]
                        list_of_tweets.insert(0, q)
                    return render_template('authorized/account.html', list_of_tweets=list_of_tweets, message=message, num_tweet=num_tweet, num_friend=num_friend, username=session['friend'], msg=session['friend'])
            model.add_friend(session['user_id'],y)
            tweets = model.list_tweets(session['friend'])
            list_of_tweets = []
            for _ in tweets:
                q = [_[1],_[2],_[3]]
                list_of_tweets.insert(0, q)
            return render_template('authorized/account.html', list_of_tweets=list_of_tweets, num_tweet=num_tweet, num_friend=num_friend, username=session['friend'], msg=session['friend'])
        elif session['friend_id']:
            num_tweet = model.find_num_tweet(session['friend_id'])
            num_friend = len(model.find_all_friend(session['friend_id']))
            x = model.find_all_friend(session['user_id'])
            for _ in range(len(x)):
                if x[_][1] == y:
                    message = 'You already followed ' + y + '.'
                    tweets = model.list_tweets(session['friend_id'])
                    list_of_tweets = []
                    for _ in tweets:
                        q = [_[1],_[2],_[3]]
                        list_of_tweets.insert(0, q)
                    return render_template('authorized/account.html', list_of_tweets=list_of_tweets, message=message, num_tweet=num_tweet, num_friend=num_friend, username=session['friend_id'], msg=session['friend_id'])
            model.add_friend(session['user_id'],y)
            tweets = model.list_tweets(session['friend_id'])
            list_of_tweets = []
            for _ in tweets:
                q = [_[1],_[2],_[3]]
                list_of_tweets.insert(0, q)
            return render_template('authorized/account.html', list_of_tweets=list_of_tweets, num_tweet=num_tweet, num_friend=num_friend, username=session['friend_id'], msg=session['friend_id'])
    
@controller.route('/re_tweet',methods=['GET','POST'])
def re_tweet():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        x = request.form['re_tweet1']
        y = request.form['re_tweet2']
        Content = y + ' \"re-sup from ' + x + '\"'
        t = str(dt.datetime.now())
        time_now = t[:19]
        num_tweet = model.find_num_tweet(session['user_id']) + 1
        model.add_tw(session['user_id'],Content,time_now)
        model.add_num(session['user_id'],num_tweet)
        User_ID=session['user_id']
        num_tweet = model.find_num_tweet(session['user_id'])
        num_friend = len(model.find_all_friend(session['user_id']))
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            list_of_friend = []
            qq = model.find_all_friend(session['user_id'])
            for __ in qq:
                list_of_friend.append(__[1])
            if _[1] in list_of_friend:
                q = [_[1],_[2],_[3]]
                list_of_tweets.insert(0, q)
            elif _[1] == session['user_id']:
                q = [_[1],_[2],_[3]]
                list_of_tweets.insert(0, q)
        return render_template('authorized/newsfeed.html', num_tweet=num_tweet, num_friend=num_friend, list_of_tweets=list_of_tweets, User_ID=User_ID)

@controller.route('/me',methods=['GET'])
def me():
    if request.method == 'GET':
        friends = model.find_all_friend(session['user_id'])
        list_of_friends = []
        for __ in friends:
            list_of_friends.append(__[1])
        tweets = model.list_tweets(session['user_id'])
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        num_tweet = model.find_num_tweet(session['user_id'])
        num_friend = len(model.find_all_friend(session['user_id']))
        return render_template('authorized/me.html', list_of_friends=list_of_friends, list_of_tweets=list_of_tweets, num_tweet=num_tweet, num_friend=num_friend, username=session['user_id'])

@controller.route('/admin',methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        users = model.suggest_friend()
        list_of_users = []
        for __ in users:
            list_of_users.append(__[0])
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        return render_template('unauthorized/admin.html', list_of_users=list_of_users, list_of_tweets=list_of_tweets)
    elif request.method == 'POST':
        name = request.form['delete1']
        time = request.form['delete2']
        model.delete_tweet(name,time)
        num_tweet = model.find_num_tweet(name) - 1
        model.add_num(name,num_tweet)
        users = model.suggest_friend()
        list_of_users = []
        for __ in users:
            list_of_users.append(__[0])
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        return render_template('unauthorized/admin.html', list_of_users=list_of_users, list_of_tweets=list_of_tweets)

@controller.route('/admin1',methods=['GET', 'POST'])
def admin1():
    if request.method == 'GET':
        users = model.suggest_friend()
        list_of_users = []
        for __ in users:
            list_of_users.append(__[0])
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        return render_template('unauthorized/admin.html', list_of_users=list_of_users, list_of_tweets=list_of_tweets)
    elif request.method == 'POST':
        a = request.form['delete3']
        for _ in model.suggest_friend():
            _[0]
            for __ in model.find_all_friend(_[0]):
                if __[1] == a:
                    model.delete_users1(_[0],a)

        model.delete_users(a)
        model.delete_tweet1(a)
        users = model.suggest_friend()
        list_of_users = []
        for __ in users:
            list_of_users.append(__[0])
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        return render_template('unauthorized/admin.html', list_of_users=list_of_users, list_of_tweets=list_of_tweets)
