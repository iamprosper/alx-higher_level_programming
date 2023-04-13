#!/usr/bin/python3
"""This module indents a text"""


def text_indentation(text):
    """Indents a text"""
    if (type(text) is not str):
        raise TypeError("text must be a string")
    chs = ['.', ':', '?']
    no_space = False
    for lt in text:
        if lt in chs:
            print("{}\n".format(lt))
            no_space = True
        else:
            if lt == " " and no_space:
                pass
            else:
                no_space = False
                print(lt, end="")
