#!/usr/bin/python3
"""A module containing a script for adding / loading cli args to json file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


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
