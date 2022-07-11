#!/usr/bin/python3
""" A module containing a single class
    Class:
        -Rectangle
"""
from .base import Base


class Rectangle(Base):
    """ Rectangle class, containing constructor, getters and setters """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """ width getter """
        return self._width

    @width.setter
    def width(self, width):
        """ width setter """
        self._width = width

    @property
    def height(self):
        """ height getter """
        return self._height

    @height.setter
    def height(self, height):
        """ height setter """
        self._height = height

    @property
    def x(self):
        """ x getter """
        return self._x

    @x.setter
    def x(self, x):
        """ x setter """
        self._x = x

    @property
    def y(self):
        """ y getter """
        return self._y

    @y.setter
    def y(self, y):
        """ y setter """
        self._y = y
