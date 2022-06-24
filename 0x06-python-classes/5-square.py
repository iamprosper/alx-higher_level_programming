#!/usr/bin/python3

"""
    A module representing a single Square class with:
    -size attribute which is a private instance attribute
    The size attribute is validated
    There is a function that prints the square
"""


class Square:

    """A Square class"""

    def __init__(self, size=0):

        """Default constructor

        Args:
            size (int): The first parameter
        """
        self.size = size

    @property
    def size(self):
        """Size guetter

        Returns:
            The value of the square size.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Size setter

        Args:
            size (int): The first parameter
        """
        if(isinstance(size, int)):
            if(size < 0):
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = size

    def area(self):
        """Square area calculator

        Returns:
            The area of the square
        """
        return(self.__size ** 2)

    def my_print(self):
        """Square printing with # character"""
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print('#', end=" ")
                print()
