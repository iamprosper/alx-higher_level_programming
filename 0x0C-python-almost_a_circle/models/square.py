#!/usr/bin/python3
""" A module containing a single class:
    Class:
        -Square - Inherit from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ A class describin a square object.
    It contains constructor an modifiers
    """

    def __init__(self, size, x=0, y=0, id=None):
        """The constructor"""
        super().__init__(size, size, x, y, id)
        # self._all_attrs = ["id", "_width", "_x", "_y"]

    def __str__(self):
        """Print the content of the object"""
        desc = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return desc.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """The size setter"""
        self.width = size
        self.height = size
