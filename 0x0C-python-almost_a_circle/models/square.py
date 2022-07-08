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
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise TypeError("size must be > 0")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the content of the object"""
        desc = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return desc.format(self.id, self.x, self.y, self.width)
