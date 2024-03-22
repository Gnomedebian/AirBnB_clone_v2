#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greetHbnb():
    '''function returns hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''function returns HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''function returns variable'''
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_py(text='is cool'):
    '''function returns variable'''
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
