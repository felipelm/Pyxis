#!/usr/bin/env python

from flask import Flask, Response, render_template, flash, session, request, redirect
import os
import datetime
import jwt

app = Flask(__name__)

@app.route("/check")
def check():
    try:
        if session['logged_in']:
            return Response('Login OK', 200, {})
        else:
            return Response('Login Required', 401, {})
    except:
        session['logged_in'] = False
        return Response('Login Required', 401, {})

@app.route("/login")
def login():
    rd = request.args.get('rd')

    return render_template('login.html', rd=rd)


@app.route('/login', methods=['POST'])
def do_login():
    if request.form['password'] == '123' and request.form['username'] == '123':
        session['logged_in'] = True
        return redirect(request.form['rd'], code=302)
    else:
        flash('wrong password!')
    return check()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return check()

if __name__ == '__main__':
    app.secret_key = '29cSy004wj2931m'
    app.run(port=os.environ.get('PORT', '7000'),
            host=os.environ.get('HOST', '0.0.0.0'))
