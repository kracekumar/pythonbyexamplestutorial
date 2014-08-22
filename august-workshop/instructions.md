#### Getting started

- Create a file `framework.py` and create class `new_app.py` will contain all details about the app.
- Create a class `App` in `framework.py` with `process_request(self)`, `run(self, port=8080)`,
  `add_route(self, route, entry_point, allowed_methods=['GET'])`, `entry(self, environment, start_response)`.
  Add `self.routes` which is a list in `__init__`.

#### Minimal Framework
- Create a new `App` object in `new_app.py` and register one single view `index` for path `/`. Then do `app.run`.
- Implement `entry`. Print the environment variable.
- Call `process_request` which should return `Response` object.
- Create a new class `Response` with `body, status, content_type, content_length` as attributes passed via
`__init__`.
- Create a `iter_body` which returns `[self.body]`.
- Create `headers` property which returns list of tuples containing `Content-Type` and `Content-Length`.
- Return `resp.iter_body` in `entry`.

- Implement `process_request`. Extract `path`, `method`.
- Iterate over the `routes` and if pattern is matched, call the view and return `Response` with status `200` else
`404`.
- Check if the method is allowed if not return `405` status code.
- Implement `add_route` where `entry_point` should be callable.
- Add more routes with different patterns like `/\d$`, `/(\d)/(\d)$`.
- Add an endpoint called `/json` which should return json.
- Add `jsonify(*args, **kwargs)` function in `framework.py` with return `Response` object where
`content_type='application/json`.

#### Add template support
- We will use `jinja2` for templating.
- Add a  method `render_template(template_name, app_name='', template_dir='', **context)`
in `framework.py`. `render_template` should return a response if template is found with
`content_type='text/html'` else `404` with `Template not found` in the body.
- By default we will consider `templates` directory to contain all templates.
- Create a environment inside `render_template` and use `get_template` to load the template.
- Change the `index` function use `render_template` and return html file.

#### Add static file support
- Add `static=True` in `App's __init__` . Add a route `/static/(.*)` and `serve_static` as callable.
- Create a new function `serve_static(path)` which looks inside `/static` directory and servers the static
  content.
- Use `mimetypes.guess_type` to guess `mimetype` of static file. If static file is found return `Respone` with
  `200`, `content_type`, `content_length` else return `404`.
- Edit `index.html` to have image in html file.

#### Add form support
- Create a new class `Request` class with `path, method, query_string, body` attributes and `environment` is passed
  as second argument in `__init__`.
- Add a method `extract_post_data(environemnt)` which extracts form data if `input CONTENT_TYPE is application/x-www-form-urlencoded'`.
- Read `wsgi.input` and parse the form content using `cgi.parse_qs`. `self.body` should contain form data as dictionary.
- If `input content is application/json` `extract_post_data` should handle it.

#### Wtforms

- Create `SimpleMultidict` in `framework.py` which has `getlist` method.
- Make `request.body` uses it.
- Create `RegistrationForm` with `username with 4 characters as minimum` and `email with minimum of 6 characters`.
- Validate the form on Post, hook to new route `/post_form`.
