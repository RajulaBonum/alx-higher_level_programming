#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle by: (based on 1-rectangle.py).

    Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.
    
        Args:
        width (int, optional): width of rectangle. Defaults to 0.
        height (int, optional): height of rectangle. Defaults to 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriver.

        Returns:
        int: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """height retriver
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of a rectangle.

        Returns:
        int: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter of a rectangle

        Returns:
        int: perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
