# -*- coding: utf-8 -*-
from bowl import App, jsonify, render_template
from wtforms import Form, StringField, validators

app = App()


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])


def post_form(request):
    form = RegistrationForm(request.body, data={'username': 'Krace'})
    if form.validate() and request.method == 'POST':
        print form.data
        return "Done"
    return str(form.data)

app.add_route('/post_form', post_form, ['GET', 'POST'])


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
