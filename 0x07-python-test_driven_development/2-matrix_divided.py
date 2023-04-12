#!/usr/bin/python3
"""This module divide a matrix"""


def matrix_divided(matrix, div):
    """This function is responsible of the operation"""
    m = [cl[:] for cl in matrix]
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    size = 0
    for cl in m:
        for value in cl:
            if (type(value) is not int and type(value) is not float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if (size != 0):
            if (size != len(cl)):
                raise TypeError("Each row of the matrix must have "
                                "the same size")
            continue
        else:
            size = len(cl)
    idx = 0
    for cl in m:
        while idx < len(cl):
            cl[idx] = round(cl[idx] / div, 2)
            idx += 1
        idx = 0
    return (m)
