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


@app.route('/c/<text>')
def text(text):
    '''function returns variable'''
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
