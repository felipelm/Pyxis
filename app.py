#!/usr/bin/env python

from flask import Flask, Response, render_template, flash, session, request
import os
import datetime
import jwt

app = Flask(__name__)

@app.route("/")
def index():
    return "Oi"

@app.route("/login_error")
def login_error():
    return Response('Login Required', 401, {})


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == '123' and request.form['username'] == '123':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

if __name__ == '__main__':
    app.secret_key = '29cSy004wj2931m'
    app.run(port=os.environ.get('PORT', '7000'),
            host=os.environ.get('HOST', '0.0.0.0'))
