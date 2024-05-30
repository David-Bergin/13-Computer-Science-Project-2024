import sqlite3
from bottle import route, view, run, debug, template, request, static_file, error, redirect



@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
@view('homepage')
def index():
    pass

run(host='localhost', port=8080)