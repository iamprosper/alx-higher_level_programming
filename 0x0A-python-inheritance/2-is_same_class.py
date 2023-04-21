#!/usr/bin/python3
""" A module containing a single function
    is_same_class(obj, a_class)

    Return: True if the obj is an instance of a_class, false otherwise
"""


def is_same_class(obj, a_class):
    """The operating function"""
    return isinstance(obj, a_class)
