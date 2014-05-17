# -*- coding: utf-8 -*-

import sys

# Write a function which returns greeting message depending on usernames


def greeting(*names):
    msg = ""
    for name in names:
        msg += "Welcome {}\n".format(name)
    return msg


def test_greeting():
    assert "python" in greeting("python")
    res = greeting("python", "emacs")
    assert "python" in res
    assert "emacs" in res


# Write a function which returns greeting message depending on usernames
# and number of times greetings needs to be printed

def greeting_with_times(**kwargs):
    msg = ""
    for name, times in kwargs.iteritems():
        for time in range(times):
            msg += "Welcome {}\n".format(name)
    return msg


def test_greeting_with_times():
    res = greeting_with_times(python=2, emacs=3)
    assert res.count("python") == 2
    assert res.count("emacs") == 3
    res = greeting_with_times(krace=0)
    assert res.count("krace") == 0


# Python scopes locals(), globals(), nested functions.

# Write a function called cache which will cache factorial result.
# When factorial is called with same number argument as previous call
# fetch result from cache.

cached_results = {}

def cache(f):

    def inner(n):
        if n in cached_results:
            print "cached_results"
            return cached_results[n]
        cached_results[n] = f(n)
        return cached_results[n]
    return inner


@cache
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# test


def test_factorial():
    assert factorial(1) == 1
    assert 1 in cached_results

# Write a function called login which will take a parameter username.
# Write a decorator called login_required which is on top of login.
# login_decorator will look into listed of predefined username and
# return True or False

def login_required(f):
    def wrapped(*args, **kwargs):
        username = kwargs['username']
        if username in ['kracekumar', 'admin']:
            return f(*args, **kwargs)
        else:
            return False
    return wrapped

@login_required
def login(username):
    print "login succeeded"
    return True


def test_login():
    assert login({}, username="kracekumar") is True
    assert login({}, username="demo") is False


def test():
    print("test_greeting")
    test_greeting()
    print("test_greeting_with_times")
    test_greeting_with_times()
    print("test_factorial")
    test_factorial()
    print("test_login")
    test_login()

def main():
    pass


if __name__ == "__main__":
    if 'test' in sys.argv:
        test()

    main()
