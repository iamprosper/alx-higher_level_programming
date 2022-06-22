#!/usr/bin/python3

"""
    A module representing a single Square class with size attribute.
    The size attribute is validated
"""


class Square:

    """A Square class"""

    def __init__(self, size=0):

        """Default constructor

        Args:
            size (int): The first parameter
        """
        if(isinstance(size, int)):
            if(size < 0):
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size

    def get_size(self):
        """Size guetter

        Returns:
            The value of the square size.
        """
        return self.__size

    def set_size(self, size):
        """Size setter

        Args:
            size (int): The first parameter
        """
        self.__size = size
