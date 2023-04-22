#!/usr/bin/python3
"""This module contain a single class
   Class:
        Square
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Base Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
