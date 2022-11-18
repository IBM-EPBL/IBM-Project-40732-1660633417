#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:32:54 2022

@author: maryada
"""

from flask import Flask,redirect,request,render_template,url_for,session
import ibm_db
import re 

app=Flask(__name__)
app.secret_key='a'
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ygg09863;PWD=dQXLECjtaCqXsJUt;","","")

@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    global userid;
    msg=" "
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
        username=request.form['username']
        password=request.form['password']
        sql="SELECT * FROM users WHERE username=? AND password=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['Loggedin']=True
            session['id']=account['USERNAME']
            userid=account['USERNAME']
            session['username']=account['USERNAME']
            msg="Logged in successfully!"
            return render_template("index.html", msg=msg)
        else :
            msg="Incorrect username and password"
            
    return render_template("login.html", msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/register",methods=["GET","POST"])
def register():
    msg=""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        sql="SELECT * from users WHERE username=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            insert_sql="INSERT INTO users VALUES(?,?,?)"
            prep_stmt=ibm_db.prepare(conn,insert_sql)
            ibm_db.bind_param(prep_stmt,1,username)
            ibm_db.bind_param(prep_stmt,2,email)
            ibm_db.bind_param(prep_stmt,3,password)
            ibm_db.execute(prep_stmt)
            msg="You have successfully logged in!"
            
    elif request.method=="POST":
        msg="Please fill out the form"
    return render_template('register.html', msg=msg)

if __name__=="__main__":
    app.run(host='0.0.0.0')