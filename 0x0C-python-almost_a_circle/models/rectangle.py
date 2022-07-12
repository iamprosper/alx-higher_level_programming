#!/usr/bin/python3
""" A module containing a single class
    Class:
        -Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class, containing constructor, getters and setters """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.__y = y

    def area(self):
        """ Area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Display the rectangle with # character """
        for yy in range(self.y):
            print("")
        for h in range(self.height):
            for xx in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print('#', end="")
            print("")

    def __str__(self):
        """ Overring/Customizing print (verbose) function """
        desc = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return desc.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update attributes values)
            Args:
                -id: The identifier of the object
                -width: The width of the rectangle
                -height: The height of the rectangle
                -x: The x coordinate of the rectangle
        """
        if len(args) > 0:
            idx = 0
            while idx < len(args):
                # self.__dict__[all_attrs[idx]] = args[idx]
                all_attrs = ["id", "_width", "_height", "_x", "_y"]
                setattr(self, all_attrs[idx], args[idx])
                idx += 1
        else:
            for key, value in kwargs.items():
                if key != "id":
                    real_key = "__" + key
                else:
                    real_key = key
                # idx = self._all_attrs.index(real_key)
                setattr(self, real_key, value)

    def to_dictionary(self):
        self_dict = {}
        attrs_to_see = ["id", "width", "height", "x", "y"]
        for attr in attrs_to_see:
            key = ""
            if attr != "id":
                key = "__" + attr
            else:
                key = attr
            self_dict[attr] = self.__dict__.get(key)
        return self_dict
