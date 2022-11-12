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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor"""
        Rectangle.number_of_instances += 1
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
                # str_value = "".join([str_value, self.print_symbol.__str__()])
                str_value += self.print_symbol.__str__()
            if (i + 1 < self.height):
                str_value += "\n"
        return str_value

    def __repr__(self):
        """Representation value of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Rectangle deletion notifier"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Rectangle comparison"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2, must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        return rect_2
