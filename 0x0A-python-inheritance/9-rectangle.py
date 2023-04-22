#!/usr/bin/python3
"""This module contain a single class
   Class:
        Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Base Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        return (self.__width * self.__height)

    def str():
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
