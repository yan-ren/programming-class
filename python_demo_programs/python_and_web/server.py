'''
Flask

Flask is a lightweight library for web development in Python
'''
import datetime
import os
import sys

from flask import Flask, render_template, request

app = Flask(__name__)


# root url/home url
@app.route('/')
def root():
    return render_template('index.html')


@app.route('/second')
def second():
    return "This is the second page"


@app.route('/second/<name>')
def name(name):
    return 'Welcome ' + name


@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", data=result)


'''
In terminal type:
export FLASK_APP=you_python_file_name.py
flask run
'''
