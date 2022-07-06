#!/usr/bin/python3
""" A module containing a single function
    Function:
        -load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ A function that create a python object from json file
        Args:
            -filename: The json's file name
    """
    obj = None
    with open(filename, 'r') as f:
        obj = json.loads(f.read())
        f.close()
    return obj
