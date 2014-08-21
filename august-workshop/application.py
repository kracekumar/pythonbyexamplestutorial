# -*- coding: utf-8 -*-
from bowl import App, jsonify, render_template

app = App()


def index(request):
    return render_template('index.html', name='Kracekumar', lang='Python')


def foo(request):
    return 'foo'


def return_int(request):
    return 2


def add(request, a, b):
    return int(a) + int(b)


def json(request):
    return jsonify(foo='foo',
                   bar='bar',
                   baz='baz')


def post(request):
    return request.body


# Register urls
app.add_route('/index', index, allowed_methods=['GET', 'POST'])
app.add_route('/post', post, allowed_methods=['GET', 'POST'])
app.add_route('/foo', foo)
app.add_route('/\d$', return_int)
app.add_route('/(\d)/(\d)$', add)
app.add_route('/json', json)


if __name__ == "__main__":
    app.run(port=8080)
