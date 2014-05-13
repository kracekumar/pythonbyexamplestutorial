# -*- coding: utf-8 -*-

import sys


def flatten(items, result=None):
    if not result:
        result = []

    for item in items:
        if isinstance(item, list):
            flatten(item, result)
        else:
            result.append(item)

    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def test_flatten():
    assert flatten([1, 2, [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([1, 2, (3, 4), "welcome"]) == [1, 2, (3, 4), "welcome"]


def test_factorial():
    assert factorial(1) == 1
    assert factorial(-1) == 1
    assert factorial(5) == 120


def test():
    print("test_flatten")
    test_flatten()
    print("test_factorial")
    test_factorial()


def main():
    pass


if __name__ == "__main__":
    if 'test' in sys.argv:
        test()
        exit(0)

    main()
