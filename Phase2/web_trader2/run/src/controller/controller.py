#!/usr/bin/env python3

from flask import Blueprint, request, render_template, session
import src.model.model as model
import sqlite3


controller = Blueprint('controller',__name__)

@controller.route('/',methods=['GET'])
def frontpage():
    if request.method == 'GET':
        return render_template('frontpage.html')


@controller.route('/loggin',methods=['GET','POST'])
def log_in():
    if request.method == 'GET':
        return render_template('loggin.html')
    elif request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id and password:
            try:
                message = '{}\'s current balance is '.format(user_id) + str(model.loggin(user_id,password))
                return render_template('web_trader.html', message=message)
            except TypeError:
                message = 'Invalid username and password.'
                return render_template('loggin.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('loggin.html', message=message)

@controller.route('/loggin_new',methods=['GET','POST'])
def log_in_new():
    if request.method == 'GET':
        return render_template('loggin_new.html')
    elif request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id and password:
            try:
                model.sign_up(user_id, password)
                message = 'You have successfully created new user.' 
                return render_template('loggin_new.html', message=message)
            except sqlite3.IntegrityError:
                message = 'Username is already exist.'
                return render_template('loggin_new.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('loggin_new.html', message=message)

@controller.route('/web_trader',methods=['GET','POST'])
def main_page():
    if request.method == 'GET':
        return render_template('web_trader.html'), user_id
    elif request.method == 'POST':
        pass

@controller.route('/lookup_quote',methods=['GET','POST'])
def lookup_quote():
    if request.method == 'GET':
        return render_template('lookup_quote.html')
    elif request.method == 'POST':
        ticker = request.form['ticker_symbol']
        company = request.form['company_name']
        if ticker:
            message1 = 'The last price for ' + str(ticker) + ' is ' + str(model.quote(ticker))
            return render_template('lookup_quote.html', message1=message1)
        elif company:
            message2 = 'The ticker symbol for ' + str(company) + ' is ' + str(model.lookup(company))
            return render_template('lookup_quote.html', message2=message2)

@controller.route('/buy',methods=['GET','POST'])
def buy():
    if request.method == 'GET':
        return render_template('buy.html')
    elif request.method == 'POST':
        ticker = request.form['ticker_symbol']
        volume = request.form['volume']
        sell_buy = 'Buy'
        trade_price = float(model.quote(ticker))
        total = float(model.quote(ticker)) * float(volume)
        if ticker and volume:
            message = "You have purchased " + str(ticker) + " volume of " + str(volume)
            message1 = "The total price you spent is " + str(float(model.quote(ticker)) * float(volume))
            model.add_buy(user_id, sell_buy, ticker, trade_price, volume, total)
            return render_template('buy.html', message=message, message1=message1)
        else:
            message = 'Fill out all category.'
            return render_template('buy.html', message=message)

@controller.route('/sell',methods=['GET','POST'])
def sell():
    if request.method == 'GET':
        return render_template('sell.html')
    elif request.method == 'POST':
        ticker = request.form['ticker_symbol']
        volume = request.form['volume']
        sell_buy = 'Sell'
        # user_id = 'kim'
        trade_price = float(model.quote(ticker))
        total = float(model.quote(ticker)) * float(volume)
        if ticker and volume:
            message = "You have sold " + str(ticker) + " volume of " + str(volume)
            message1 = "The total price you earned is " + str(float(model.quote(ticker)) * float(volume))
            model.add_sell(user_id, sell_buy, ticker, trade_price, volume, total)
            return render_template('sell.html', message=message, message1=message1)
        else:
            message = 'Fill out all category.'
            return render_template('sell.html', message=message)