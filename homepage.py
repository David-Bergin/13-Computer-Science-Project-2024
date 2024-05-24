from bottle import run, route, view, static_file, request



@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
@view('homepage')
def index():
    pass