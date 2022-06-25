#!/usr/bin/python3

"""
    A module representing a single Square class with:
    -size attribute which is a private instance attribute
    The size attribute is validated
    There is a function that prints the square
    The square is positioned whitin a grid
"""


class Square:

    """A Square class"""

    def __init__(self, size=0, position=(0, 0)):

        """Default constructor

        Args:
            size (int): The first parameter
            postition (tuple): The second parameter
        """
        self.size = size
        self.position = position
        self.__valid = True

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

    @property
    def position(self):
        """Position guetter

        Returns:
            The value of the square position.
        """
        return self.__position

    @position.setter
    def position(self, position):
        """Position setter

        Args:
            position (tuple): The first parameter
        """
        if(isinstance(position, tuple)):
            if(len(position) != 2 or position[0] < 0
                    or position[1] < 0):
                raise TypeError(("position must be a "
                                 "tuple of 2 positive integers"))
                self.__valid = False
        else:
            raise TypeError(("position must be a "
                             "tuple of 2 positive integers"))
            self.__valid = False
        self.__position = position

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
        elif self.size > 0 and self.__valid:
            for x in range(self.size):
                for p1 in range(self.position[0]):
                    print(" ", end="")
                for y in range(self.size):
                    print('#', end="")
                print()
