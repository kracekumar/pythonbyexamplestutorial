# -*- coding: utf-8 -*-
"""
Bowl is web framework for learning how web framework works.
"""
import re
import json
import mimetypes
import os
from cgi import parse_qs
from jinja2 import Environment, PackageLoader, TemplateNotFound


def jsonify(*args, **kwargs):
    jsonified = json.dumps(dict(*args, **kwargs),
                           indent=2)
    return Response(body=jsonified,
                    status='200',
                    content_type='application/json')


def serve_static(path):
    parts = path.split('/')
    full_path = os.path.sep.join(['static'] + parts)
    try:
        with open(full_path, 'rb') as f:
            mime_type = mimetypes.guess_type(full_path)[0] or 'text/plain'
            filesize = int(os.path.getsize(full_path))
            return Response(body=f.read(),
                            content_type=mime_type,
                            content_length=filesize)
    except IOError:
        return Response(status='404')


def render_template(template_name, app_name='', template_dir='', **context):
    if template_dir:
        env = Environment(loader=PackageLoader(template_dir))
    else:
        env = Environment(loader=PackageLoader('application', 'templates'))
    try:
        template = env.get_template(template_name)
    except TemplateNotFound as e:
        return Response(body="Template not found: {}".format(e),
                        status='404')
    return Response(body=template.render(**context),
                    content_type='text/html')


class Response(object):
    def __init__(self, body=None, status='200', content_type='text/plain',
                 content_length=None):
        self.body = str(body)
        self.status = status
        self.content_type = content_type
        self.content_length = content_length or len(self.body)

    def iter_body(self):
        return [self.body]

    @property
    def headers(self):
        return [('Content-type', self.content_type),
                ('Content-Length', self.content_length,)]


class Request(object):
    def __init__(self, environment):
        self.path = environment.get('PATH_INFO')
        self.method = environment.get('REQUEST_METHOD')
        self.query_string = environment.get('QUERY_STRING')
        self.body = {}
        if self.method == 'POST':
            self.extract_post_data(environment)

    def extract_post_data(self, environment):
        if environment.get('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
            input = environment.get('wsgi.input')
            size = int(environment.get('CONTENT_LENGTH'))
            self.body = parse_qs(input.read(size))
            input.close()


class App(object):
    """App class contains all details about the application to run.
    """
    def __init__(self, static=True):
        # Routes will contain nested list where first item is pattern and
        # second item is view_func, third item is list of allowed_methods
        self.routes = []
        if static:
            self.add_route('/static/(.*)', serve_static)

    def process_request(self):
        path = self.environment.get('PATH_INFO')
        method = self.environment.get('REQUEST_METHOD')

        for pattern, view_func, methods in self.routes:
            match = re.match('^' + pattern + '$', path)
            if match:
                args = match.groups()
                if method in methods:
                    request = Request(self.environment)
                    resp = view_func(request, *args)
                    if isinstance(resp, Response):
                        return resp
                    return Response(body=resp)
                else:
                    return Response(body='Not Allowed', status='405')
        else:
            return Response(body='Not found', status='404')

    def entry(self, environment, start_response):
        self.environment = environment
        resp = self.process_request()
        start_response(resp.status, resp.headers)
        return resp.iter_body()

    def add_route(self, route, entry_point, allowed_methods=['GET']):
        if callable(entry_point):
            methods = [method.upper() for method in allowed_methods]
            self.routes.append([route, entry_point, methods])
        else:
            raise TypeError("{} for {} is not callable".format(entry_point, route))

    def run(self, port=8000):
        from werkzeug.serving import run_simple
        run_simple('127.0.0.1', port, self.entry, use_debugger=True,
                   use_reloader=True)


if __name__ == "__main__":
    print("Nothing here. This needs to be imported somewhere")
