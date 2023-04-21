#!/usr/bin/python3
""" A module containing a single class
    Class:
        -MyList
"""


class MyList(list):
    """ A class containing a single function
        Function name:
            -print_sorted(self)
    """
    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
