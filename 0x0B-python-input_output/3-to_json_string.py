#!/usr/bin/python3
""" A module containing a single function
    Function:
        -to_json_string(my_obj)
"""
import json


def to_json_string(my_obj):
    """ A function that serialize a json object to python one's
        Args:
            -my_obj: The python object
    """
    return json.dumps(my_obj)
