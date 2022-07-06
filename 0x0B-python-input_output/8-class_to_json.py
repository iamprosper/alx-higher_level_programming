#!/usr/bin/python3
""" A module containing a single function
    function:
        -class_to_json
"""


def class_to_json(obj):
    """ A function that serialize a class
        Args:
            -obj: The class to serialize
    """
    return obj.__dict__
