#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''function returns n is number'''
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    '''Displays an HTML page only if <n> is an integer'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''even or odd'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
