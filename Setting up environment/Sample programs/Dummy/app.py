#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:54:36 2022

@author: maryada
"""

from flask import Flask,redirect,url_for,request
app=Flask(__name__)
@app.route('/success/<name>')
def success(name):
    return "welcome %s" %name
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form["nm"]
        return redirect(url_for('success',name = user))


if __name__=='__main__':
    app.run(debug=True)