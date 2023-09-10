#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Attributes of the rectangle"""

    @property
    def width(self):
        """returns widith"""
        return self.__width

    @width.setter
    def width(self, value):
        """property settler"""
        if not isinstance(value, int):
            raise TypeError("width must be and integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property settler"""
        if not isinstance(value, int):
            raise TypeError("height must be and integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """creates new instances"""

        self.height = height
        self.width = width
