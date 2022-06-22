#!/usr/bin/python3

"""
    A module representing a single Square class with:
    -size attribute.
    The size attribute is validated
"""


class Square:

    """A Square class"""

    def __init__(self, size=0):

        """Default constructor

        Args:
            size (int): The first parameter
        """
        try:
            if(isinstance(size, int)):
                try:
                    if(size < 0):
                        raise ValueError("size must be >= 0")
                except ValueError as ve:
                    print(ve)
                    size = 0
            else:
                raise TypeError("size must be an integer")
        except TypeError as te:
            print(te)
            size = 0

        self.__size = size
        self.area = self.__size ** 2

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

    def area(self):
        """Square area calculator

        Returns:
            The area of the square
        """
        return(self.area)
