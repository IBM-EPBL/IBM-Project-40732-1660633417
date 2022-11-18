#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:51:02 2022

@author: maryada
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
   return render_template("index.html")
if __name__ == '__main__':
   app.run(debug = True)