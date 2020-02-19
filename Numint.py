"""we are going to make a pretty file to do numerical integration v1"""
import numpy as np


def simpson(f0, f1, f2, x0, x2):
    h = (x2 - x0) / 2
    return h / 3 * (f0 + 4 * f1 + f2)


def trapezoid(f0, f1, x0, x1):
    return (x1 - x0) / 2 * (f0 + f1)


def comp_num_int(x_lst, f_lst):
    """input coordinates and the function values at those coordinate as two lists of the same length. Include a point
    at the beginning and end """

    function_sum = 0

    # Check length of array for compatibility with simpson
    if len(x_lst) == len(f_lst):
        i = 0
        while i < len(x_lst) - 2:
            function_sum += simpson(f_lst[i], f_lst[i + 1], f_lst[i + 2], x_lst[i], x_lst[i + 2])
            i += 2

        if i != len(x_lst):
            # do trap rule
            while i != len(x_lst) - 1:
                function_sum += trapezoid(f_lst[i], f_lst[i + 1], x_lst[i], x_lst[i + 1])

                i += 1

    else:
        raise Exception('Not equal number of points as function values')
    return function_sum
