#!/usr/bin/python3

"""A module representing a single Square class with size attribute"""


class Square:

    """A Square class"""

    def __init__(self, size):

        """Default constructor"""

        self.__size = size

    def get_size(self):
        """Size guetter"""
        return self.__size

    def set_size(self, size):
        """Size setter"""
        self.__size = size
