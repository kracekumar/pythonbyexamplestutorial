# -*- coding: utf-8 -*-
import sys


def square(no):
    return no * no


def cube(square_fun, no):
    return square_fun(no) * no


def list_of_squares(nos):
    return map(square, nos)


def filter_evens(nos):
    return filter(is_even, nos)


def is_even(no):
    return no % 2 == 0


def sum_of_squares_of_even_nos(nos):
    evens = filter_evens(nos)
    squares = list_of_squares(evens)
    return sum(squares)


def test_square():
    assert square(4) == 16
    assert square(-4) == 16
    try:
        square("python")
    except TypeError:
        pass


def test_cube():
    assert cube(square, 2) != 4
    assert cube(square, 3) == 27
    assert cube(square, -3) == -27


def test_list_of_squares():
    assert list_of_squares([1, 3, 5]) == [1, 9, 25]


def test_filter_evens():
    assert filter_evens([1, 2, 4, 8]) == [2, 4, 8]


def test_sum_of_squares_of_even_nos():
    assert sum_of_squares_of_even_nos([1, 2, 4, 7]) == 20
    assert sum_of_squares_of_even_nos([]) == 0


def test():
    print("started test_square")
    test_square()
    print("started test_cube")
    test_cube()
    print("started test_list_of_squares")
    test_list_of_squares()
    print("started test_filter_evens")
    test_filter_evens()
    print("started test_sum_of_squares_of_even_nos")
    test_sum_of_squares_of_even_nos()
    print("test completed")


if __name__ == "__main__":
    if 'test' in sys.argv:
        test()
