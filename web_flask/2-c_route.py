#!/usr/bin/python3
# script that starts a flask web application


from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return ("C " + text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0")