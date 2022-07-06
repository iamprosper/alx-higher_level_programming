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
        with open(filename, 'r+', encoding="utf-8") as f:
            f.seek(0)
            ch = f.write(text)
            f.truncate()
            f.close()
            print("File contents updated")
    except FileNotFoundError as fe:
        with open(filename, 'w', encoding="utf-8") as f:
            ch = f.write(text)
            f.close()
            print("File newly created")
    return(ch)
