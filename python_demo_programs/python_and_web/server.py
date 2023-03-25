'''
Flask

Flask is a lightweight library for web development in Python
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to Flask!"

'''
In terminal type:
export FLASK_APP=you_python_file_name.py
flask run
'''