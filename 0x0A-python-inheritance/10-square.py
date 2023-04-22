#!/usr/bin/python3
"""This module contain a single class
   Class:
        Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Base Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        return (self.__size * self.__size)
