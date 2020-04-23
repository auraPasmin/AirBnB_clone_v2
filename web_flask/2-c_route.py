#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    tC = text.replace('_', ' ')
    return 'C {}'.format(tC)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
