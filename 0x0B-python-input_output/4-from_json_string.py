#!/usr/bin/python3
""" A module containing a single function
    Function:
        -from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """ A function that serialize a json object to python one's
        Args:
            -my_str: The json object
    """
    return json.loads(my_str)
