#!/usr/bin/env python3

from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def frontpage():
    if request.method == 'GET':
        message = 'welcome to the new world order'
        return render_template('index.html',message=message)
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            if username=='kenny' and password=='opensesame':
                message = 'You have successfully logged into your application'
                return render_template('index.html', message=message)
            else:
                message = 'Invalid Username and Password'
                return render_template('index.html', message=message)

@app.route('/grandpa', methods = ['GET', 'POST'])
def grandpa():
    if request.method == 'GET':
        message = 'Hello, Grandson'
        return render_template('grandpa.html',message=message)
    elif request.method == 'POST':
        forename = request.form['forename']
        message = request.form['message']
        if forename and message:
            if message==message.upper():
                message = 'Shut up, you are too loud!!'
                return render_template('grandpa.html',message=message)
            else:
                message = 'What? I can\'t hear you!!!'
                return render_template('grandpa.html',message=message)

if __name__ == '__main__':
	app.run(debug=True)
