#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/<name>')
def print_name(name):
    return 'Welcome {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
