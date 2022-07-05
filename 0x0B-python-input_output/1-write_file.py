#!/usr/bin/python3
""" A module containing a single function writing contents to a file """


def write_file(filename="", text=""):
    ch = 0
    """ A function which print add content to a file

        Args:
            -filename: The file's name
            -text: The content to add
    """
    with open(filename, 'w', encoding="utf8") as f:
        ch = f.write(text)
        f.close()
    return(ch)
