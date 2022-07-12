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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Getting the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle using # character"""
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(' ', end="")
            for w in range(self.width):
                print('#', end="")
            print("")

    def __str__(self):
        """Describing the object"""
        desc = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return desc.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Upadate an attribute/sequence of attrs"""
        atrs_list = ["id", "width", "height", 'x', 'y']
        idx = 0
        key = ""
        s_atr = "_{:s}__{:s}"
        if len(args) != 0:
            while idx < len(args):
                if idx == 0:
                    atr = "id"
                else:
                    atr = s_atr.format(self.__class__.__name__, atrs_list[idx])
                setattr(self, attr, args[idx])
                idx += 1
        else:
            for k, v in kwargs.items():
                if k != "id":
                    attr = s_atr.format(self.__class__.__name__, k)
                else:
                    attr = k
                setattr(self, attr, v)
