#!/usr/bin/python3
"""This module contain a single class
   Class:
        Rectangle
"""


class Rectangle(BaseGeometry):
    """Base Rectangle class"""
    def __init__(self, width, height):
        integer_validator("width", width)
        integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
