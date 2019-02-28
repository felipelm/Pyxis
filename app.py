#!/usr/bin/env python

from flask import Flask, Response, render_template, flash, session, request, redirect
import os
import datetime
import jwt
import ldap

app = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == '123' and password == '123'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route("/check")
def check():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    return Response('Login OK', 200, {})

@app.route("/ldap")
def ldap_auth():
  try:
    #if authentication successful, get the full user data
    connect.bind_s(user_dn,password)
    result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
    # return all user data results
    connect.unbind_s()
    return result
  except ldap.LDAPError:
    connect.unbind_s()
    return "authentication error"

if __name__ == '__main__':
    app.secret_key = '29cSy004wj2931m'
    app.run(port=os.environ.get('PORT', '7000'),
            host=os.environ.get('HOST', '0.0.0.0'))
