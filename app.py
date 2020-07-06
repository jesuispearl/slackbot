# from flask import Flask

# app = Flask(__name__)

# PORT = 4390


# @app.route('/')
# def homepage():
#     return "Howdy hacker!!!"


# if __name__ == '__main__':
#     app.run(debug=True, port=PORT)


#!/usr/bin/env python
# encoding: utf-8

from bottle import run, post


@post('/hello')
def hello():
    return'Hello World!'


if __name__ == '__main__':
    run(host='0.0.0.0', port=5000)
