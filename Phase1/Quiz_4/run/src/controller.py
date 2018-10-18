#!/usr/bin/env python3

from flask import Flask, request, render_template
from mapper import Database
import sqlite3


app = Flask(__name__)
mp = Database('Login.db')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id and password:
            try:
                with Database('Login.db') as db:
                    db.loggin(user_id,password)
                    message = 'You have successfully logged in'
                    return render_template('login.html', message=message)
            except TypeError:
                message = 'Invalid username and password.'
                return render_template('login.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('login.html', message=message)

@app.route('/login_new',methods=['GET','POST'])
def log_in_new():
    if request.method == 'GET':
        return render_template('login_new.html')
    elif request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id and password:
            try:
                with Database('Login.db') as db:
                    db.signup(user_id, password)
                    message = 'You have successfully created new user.' 
                    return render_template('login.html', message=message)
            except sqlite3.IntegrityError:
                message = 'Username is already exist.'
                return render_template('login_new.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('login_new.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)