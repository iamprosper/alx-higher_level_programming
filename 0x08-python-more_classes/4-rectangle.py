#!/usr/bin/python3
"""
    This module contain a single Rectangle class
"""


class Rectangle:
    """Rectable class
    Var:
        -width: Private instance attribute
        -height: Private instance attribute
        -area: Public instance method
        -perimeter: Public instance method
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

    def area(self):
        """Area calculation"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter calculation"""
        perimeter = (self.width + self.height) * 2
        return 0 if self.width == 0 or self.height == 0 else perimeter

    def __str__(self):
        """String representation of the rectangle"""
        if (self.width == 0 or self.height == 0):
            return ""
        str_value = ""
        for i in range(self.height):
            for j in range(self.width):
                str_value += "#"
            if (i + 1 < self.height):
                str_value += "\n"
        return str_value

    def __repr__(self):
        """Representation value of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)
