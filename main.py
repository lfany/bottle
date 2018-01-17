# from bottle import route, run, template

from bottle import route, template, run


@route('/hello/<name>')
def index(name):
    return template('<b>Hello world, {{name}}!</b>', name=name)


if __name__ == '__main__':
    run(host='localhost', port='8080')
