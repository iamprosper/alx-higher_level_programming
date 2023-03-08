#!/usr/bin/python3
def remove_char_at(string, n):
    if (n >= string.length or n < 0):
        return
    string[n] = ""
