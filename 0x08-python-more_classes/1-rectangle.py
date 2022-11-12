#!/usr/bin/python3
"""
    This module contain a single Rectangle class
"""


class Rectangle:
    """Rectable class
    Var:
        -width: Private instance attribute
        -height: Private instance attribute
    """

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
