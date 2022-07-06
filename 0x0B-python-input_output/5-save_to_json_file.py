#!/usr/bin/python3
""" A module containing a single function
    Function name:
        -save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """ A function that save a json object to a file
    Args:
        -my_obj: The json object
        -filename: The path of the file's name
    """
    with open(filename, 'w') as f:
        json_file = json.dumps(my_obj)
        f.write(json_file)
        f.close()
