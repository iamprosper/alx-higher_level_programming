#!/usr/bin/python3
"""Matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Checking function"""
    a_element_size = 0

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for element in m_a:
        if type(element) is not list:
            raise TypeError("m_a must be a list of lists")
        for value in element:
            if type(value) is not int and type(value) is not float:
                raise TypeError("m_a should contain only integers or floats")
        if a_element_size == 0:
            a_element_size = len(element)
        else:
            if len(element) != a_element_size:
                raise TypeError("each row of m_a must be of the same size")

    b_element_size = 0

    for element in m_b:
        if type(element) is not list:
            raise TypeError("m_b must be a list of lists")
        for value in element:
            if type(value) is not int and type(value) is not float:
                raise TypeError("m_b should contain only integers or floats")
        if b_element_size == 0:
            b_element_size = len(element)
        else:
            if len(element) != b_element_size:
                raise TypeError("each row of m_b must be of the same size")

    if a_element_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return (mul(m_a, m_b))


def mul(m_a, m_b):
    """Operating funcion"""
    result = np.dot(m_a, m_b)
    return (result)
