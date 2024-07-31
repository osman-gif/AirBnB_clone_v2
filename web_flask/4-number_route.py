#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>")
def c_text(text):
    return 'C ' + str(text).replace('_', ' ')


@app.route("/python")
@app.route("/python/")
@app.route("/python/<string:text>")
def python_text(text=None):
    if text:
        return "Python " + str(text).replace('_', ' ')
    else:
        return "Python is cool"


@app.route("/number/<int:n>")
def is_number(n):
    if type(n) is int:
        return str(n) + ' is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
