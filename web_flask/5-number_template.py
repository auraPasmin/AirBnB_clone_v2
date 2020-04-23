#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>:
/python/(<text>):
/number/<n>:
/number_template/<n>:
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_r(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def if_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def if_html(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
