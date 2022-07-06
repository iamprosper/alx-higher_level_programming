#!/usr/bin/python3
""" A module containing a single function for appending content to a file
    Function signature:
        -append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """ A function for appending content to a file
        Args:
            -filename: The path to the file's name
            -text: The content to append
    """
    ch = 0
    with open(filename, 'a+', encoding="utf-8") as f:
        ch = f.write(text)
        f.close()
    return ch
