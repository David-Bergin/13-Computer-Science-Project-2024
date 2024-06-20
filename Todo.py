import sqlite3
from bottle import route, view, run, debug, template, request, static_file, error, redirect

@route('/') #calls the homepage tpl folder so the user will be taken to the homepage when the to do list is run
def index():
    return template('homepage.tpl')

@route('/todo') #calls the todo page into the code
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output
#GET method to check the ID and the task so that its status can be updated
@route('/todo/<no:int>', method='GET')
def todo_list(no):
    
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
   
    if no == 2:
        c.execute("SELECT id, task FROM todo WHERE status LIKE '1' ORDER BY task ASC")
    elif no == 1:
        c.execute("SELECT id, task FROM todo WHERE status LIKE '1' ORDER BY id ASC")
    
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

#/new route allows user to create a new task and have it updated in the todo list with the help of c.execute command
@route('/new', method='GET')
def new_item():
    if 'save' in request.GET:
        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        message = 'A New Task has been entered. Good luck completing it!' # nessage variable created
        return template('message', message=message) # return the message template with the message variable
    
    else:
        return template('new_task.tpl')

#edit page and various if statements to allow user to update tasks and see the updates
@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'Todo':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        message = 'The item number %s was successfully updated' % no
        return template('message', message=message)
        
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", ([str(no)]) ) 
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

#error messages and selcting tasks from ID
@route('/item<item:re:[0-9]+>')
def show_item(item):

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
        result = c.fetchall()
        c.close()

        if not result:
            message = 'This item number does not exist!'
        else:
            message = 'Task: %s' % result[0]
        
        return template('message', message=message)


@route('/help')
def help():

    static_file('help.html', root='.')

#json route that selectes tasks from todo anc checks the ID
@route('/json<json:re:[0-9]+>')
def show_json(json):

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!<a href="/">Go back to home</a>'}
    else:
        return {'task': result[0]}

#error maesages for different circumstances
@error(403)
def mistake403(code):
    message = 'There is a mistake in your url!' 
    return template('message', message=message) 

@error(404)
def mistake404(code):
    message = 'Sorry, this page does not exist!'
    return template('message', message=message)

@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static') 

debug(True)
run(reloader=True)
