#!/usr/bin/python3
""" A module containing a single function writing contents to a file """


def write_file(filename="", text=""):
    ch = 0
    """ A function which print add content to a file

        Args:
            -filename: The file's name
            -text: The content to add
    """
    try:
        with open(filename, 'x') as f:
            ch = f.write(text)
            f.close()
    except FileExistsError as fe:
        with open(filename, 'a') as f:
            ch = f.write(text)
            f.close()
    return(ch)
