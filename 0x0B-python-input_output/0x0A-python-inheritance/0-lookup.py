#!/usr/bin/python3
""" A module containing a single function
    Function:
        -lookup(obj)
"""


def lookup(obj):
    """ A function that return all the attributes and methods of object
        Args:
            -obj: The object
    """
    return dir(obj)
