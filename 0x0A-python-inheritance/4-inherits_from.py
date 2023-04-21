#!/usr/bin/python3
""" A module containing a single function
    inherits_from(obj, a_class)

    Return: True if the obj is a subclass , false otherwise
"""


def inherits_from(obj, a_class):
    """The operating function"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
