#!/usr/bin/python3
""" Reading module containing one single function"""


def read_file(filename=""):
    """ A function with print the content of a file to stdout
        Args:
            -filename: The file's name
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
