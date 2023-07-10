from flask import Flask, render_template, request

app = Flask(__name__)


# root url/home url
@app.route('/')
def root():
    return render_template('index2.html')


@app.route('/second')
def second():
    return "This is the second page"


@app.route('/second/<name>')
def name(name):
    return 'Welcome ' + name

'''
exercise:
1. create a new path, which takes a path parameter, e.g. a string
2. the server checks if the string is palindrome or not, and return the result
'''


@app.route('/pal/<string>')
def palindrome(string):
    if string[::-1] == string:
        return string + " is palindrome"
    return string + " is not palindrome"


@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        result = request.form
        print(result)
        return render_template("result.html", data=result)
