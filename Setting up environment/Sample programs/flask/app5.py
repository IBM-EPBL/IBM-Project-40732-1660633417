#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:54:36 2022

@author: maryada
"""

from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form["unm"]
        email=request.form["email"]
        phone=request.form["phone"]
        return render_template("welcome.html", name=username,email=email,phone=phone)
    return render_template("login1.html")

if __name__=='__main__':
    app.run(debug=True)