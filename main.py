# from bottle import route, run, template

from bottle import route, template, run, get, post, request


@route('/')
@route('')
def index():
    return 'hello world!'


@route('/hello/<name>')
def index(name):
    return template('<b>Hello world, {{name}}!</b>', name=name)


@get('/login')  # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


def check_login(username, password):
    if username != None and username != '' and \
            password != None and password != '':
        return True
    else:
        return False


@post('/login')  # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct. username: %s password %s</p>" % (username, password)
    else:
        return "<p>Login failed.</p>"


if __name__ == '__main__':
    run(host='localhost', port='8080', debug=True)
