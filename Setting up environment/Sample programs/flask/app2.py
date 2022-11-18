#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:45:19 2022

@author: maryada
"""

from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)
 
if __name__ == '__main__':
   app.run(debug = True)