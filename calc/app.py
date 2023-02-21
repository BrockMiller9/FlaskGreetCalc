# Put your app in here.

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/add')
def get_add():
    a = request.args.get('a')
    b = request.args.get('b')
    return f'{int(a) + int(b)}'


@app.route('/sub')
def get_sub():
    a = request.args.get('a')
    b = request.args.get('b')
    return f'{int(a) - int(b)}'


@app.route('/mult')
def get_mult():
    a = request.args.get('a')
    b = request.args.get('b')
    return f'{int(a) * int(b)}'


@app.route('/div')
def get_div():
    a = request.args.get('a')
    b = request.args.get('b')
    return f'{int(a) / int(b)}'
