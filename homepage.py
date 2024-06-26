import sqlite3
from bottle import route, view, run, debug, template, request, static_file, error, redirect
import Todo

@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def index():
    return static_file("homepage.html", root='./')

@route('/todo') #calls the todo page into the code
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

run(host='localhost', port=8080, reloader = True)