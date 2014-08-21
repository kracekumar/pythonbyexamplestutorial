### Write your own web framework

This workshop will focus on writing your own web framework.
Idea is to learn what happens behind python framework. We will focussing
on creating framework which will receive HTTP Request and send HTTP Request.

We will try to incorporate other external libraries like Jinja2 to use with our
framework. We will not try to write WSGI adapter (`Gunicorn`) which will do all
low level stuffs like opening socket etc... We will use `werkzeug` which will
run our web framework in local.
