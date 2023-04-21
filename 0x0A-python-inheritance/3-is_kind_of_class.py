#!/usr/bin/python3
""" A module containing a single function
    is_kind_class(obj, a_class)

    Return: True if the obj is an i/d of a_class, false otherwise
"""


def is_kind_of_class(obj, a_class):
    """The operating function"""
    return True if isinstance(obj, a_class) else False
