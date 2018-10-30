#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect
import src.model.model as model
import sqlite3


controller = Blueprint('public',__name__)

@controller.route('/',methods=['GET','POST'])
def log_in():
    if request.method == 'GET':
        return render_template('loggin.html')
    elif request.method == 'POST':
        session['user_id'] = request.form['user_id']
        password = request.form['password']
        if session['user_id'] and password:
            if session['user_id'] == 'Admin' and password == '1q2w3e4r':
                return render_template('admin.html')
            else:
                try:
                    message = '{}\'s current balance is '.format(session['user_id']) + str(model.loggin(session['user_id'],password))
                    return redirect('/web_trader')
                except TypeError:
                    message = 'Invalid username and password.'
                    return render_template('loggin.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('loggin.html', message=message)



@controller.route('/admin',methods=['GET','POST'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html')
    elif request.method == 'POST':
        pass

@controller.route('/admin/history',methods=['GET','POST'])
def admin_hist():
    history = model.view_hist()
    allport = model.view_allpor()
    if request.method == 'GET':

        return render_template('admin_hist.html', history=history, allport=allport)
    elif request.method == 'POST':
        pass

@controller.route('/admin/leaderboard',methods=['GET','POST'])
def admin_leader():
    leaderboard = model.leaderboard()
    if request.method == 'GET':
        return render_template('admin_leader.html', leaderboard=leaderboard)
    elif request.method == 'POST':
        pass

@controller.route('/admin/lookup_quote',methods=['GET','POST'])
def admin_lookup():
    if request.method == 'GET':
        return render_template('admin_lookup.html')
    elif request.method == 'POST':
        ticker = request.form['ticker_symbol']
        company = request.form['company_name']
        if ticker:
            try:
                message1 = 'The last price for ' + str(ticker) + ' is ' + str(model.quote(ticker))
                return render_template('admin_lookup.html', message1=message1)
            except:
                message1 = 'Wrong Ticker Symbol'
                return render_template('admin_lookup.html', message1=message1)

        elif company:
            try:
                message2 = 'The ticker symbol for ' + str(company) + ' is ' + str(model.lookup(company))
                return render_template('admin_lookup.html', message2=message2)
            except:
                message2 = 'Wrong Company Name'
                return render_template('admin_lookup.html', message2=message2)



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
                return redirect('/')
            except sqlite3.IntegrityError:
                message = 'Username is already exist.'
                return render_template('loggin_new.html', message=message)
        else:
            message = 'Fill out both category.'
            return render_template('loggin_new.html', message=message)

@controller.route('/web_trader',methods=['GET','POST'])
def main_page():
    if request.method == 'GET':
        message = '{}\'s current balance is '.format(session['user_id']) + str(model.balance(session['user_id']))
        return render_template('web_trader.html', message=message)
    elif request.method == 'POST':
        message = '{}\'s current balance is '.format(session['user_id']) + str(model.balance(session['user_id']))
        return render_template('web_trader.html', message=message)

@controller.route('/lookup_quote',methods=['GET','POST'])
def lookup_quote():
    if request.method == 'GET':
        return render_template('lookup_quote.html')
    elif request.method == 'POST':
        ticker = request.form['ticker_symbol']
        company = request.form['company_name']
        if ticker:
            try:
                message1 = 'The last price for ' + str(ticker) + ' is ' + str(model.quote(ticker))
                return render_template('lookup_quote.html', message1=message1)
            except:
                message1 = 'Wrong Ticker Symbol'
                return render_template('lookup_quote.html', message1=message1)

        elif company:
            try:
                message2 = 'The ticker symbol for ' + str(company) + ' is ' + str(model.lookup(company))
                return render_template('lookup_quote.html', message2=message2)
            except:
                message2 = 'Wrong Company Name'
                return render_template('lookup_quote.html', message2=message2)

@controller.route('/buy',methods=['GET','POST'])
def buy():
    if request.method == 'GET':
        return render_template('buy.html')
    elif request.method == 'POST':
        try:
            ticker = request.form['ticker_symbol']
            volume = request.form['volume']
            if ticker and volume:
                user_id = session['user_id']
                sell_buy = 'Buy'
                trade_price = float(model.quote(ticker))
                try:
                    total = float(model.quote(ticker)) * float(volume)
                    if total <= model.balance(user_id):
                        model.add_buy(user_id, sell_buy, ticker, trade_price, volume, total)
                        model.change_bal(user_id,model.balance(user_id)-total)
                        message = "You have purchased " + str(ticker) + " volume of " + str(volume)
                        message1 = "The total price you spent is " + str(float(model.quote(ticker)) * float(volume))
                        try:
                            company_volume = model.fetch_vol(user_id,ticker)
                            company_volume += float(volume)
                            model.update_port(user_id, ticker, company_volume)
                        except TypeError:
                            model.insert_port(user_id, ticker, volume)
                        return render_template('buy.html', message=message, message1=message1)
                    else:
                        message = 'Not enough money.'
                        return render_template('buy.html', message=message)
                except:
                    message = 'Wrong volume number.'
                    return render_template('buy.html', message=message)
            else:
                message = 'Fill out all category.'
                return render_template('buy.html', message=message)
        except KeyError:
            message = 'Ticker symbol is invalid.'
            return render_template('buy.html', message=message)

@controller.route('/sell',methods=['GET','POST'])
def sell():
    if request.method == 'GET':
        return render_template('sell.html')
    elif request.method == 'POST':
        try:
            ticker = request.form['ticker_symbol']
            volume = request.form['volume']
            if ticker and volume:
                sell_buy = 'Sell'
                user_id = session['user_id']
                trade_price = float(model.quote(ticker))
                try:
                    total = float(model.quote(ticker)) * float(volume)
                    try:
                        volume1 = model.fetch_vol(user_id, ticker)
                        if volume <= volume1:
                            message = "You have sold " + str(ticker) + " volume of " + str(volume)
                            message1 = "The total price you earned is " + str(float(model.quote(ticker)) * float(volume))
                            model.add_sell(user_id, sell_buy, ticker, trade_price, volume, total)
                            model.change_bal(user_id,model.balance(user_id)+total)
                            company_volume = model.fetch_vol(user_id,ticker)
                            company_volume -= float(volume)
                            model.update_port(user_id, ticker, company_volume)
                            return render_template('sell.html', message=message, message1=message1)
                        else:
                            message = 'Not enough shares'
                            return render_template('sell.html', message=message)
                    except TypeError:
                        message = 'You don\'t have share of {}.'.format(ticker)
                        return render_template('sell.html', message=message)
                except:
                    message = 'Wrong volume number'
                    return render_template('sell.html', message=message)
            else:
                message = 'Fill out all category.'
                return render_template('sell.html', message=message)
        except KeyError:
            message = 'Ticker symbol is invalid.'
            return render_template('sell.html', message=message)

@controller.route('/portfolio',methods=['GET','POST'])
def portfolio():
    port = model.view_port(session['user_id'])
    if request.method == 'GET':
        message = '{}\'s portfolio.'.format(session['user_id'])
        message1 = 'Total balance including all shares are ' + str(model.balance(session['user_id'])+model.sum_val(session['user_id']))
        return render_template('portfolio.html', message=message, message1=message1, port=port)