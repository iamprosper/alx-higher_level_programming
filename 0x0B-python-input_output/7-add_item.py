#!/usr/bin/python3
"""A module containing a script for adding / loading cli args to json file"""
# save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
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


if __name__ == "__main__":
    import sys
    elements = []
    filename = "add_item.json"
    try:
        elements = load_from_json_file(filename)
    except FileNotFoundError as fe:
        save_to_json_file([], filename)
    if (len(sys.argv) > 1):
        for element in sys.argv[1:]:
            elements.append(element)
        save_to_json_file(elements, filename)
