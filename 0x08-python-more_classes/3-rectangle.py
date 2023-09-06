#!/usr/bin/python3
"""Class rectangle"""

class Rectangle:
    """This is a rectangle"""

    def __init__(self, width=0, height=0):
        """initializing a new rectagnle"""

        self.width = width
        self.height = height
    @property
    def width(self):
        """Get/set"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isintance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isintance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectngle"""
        return (self.__widt * self.__height)
    
    def perimeter(self):
        """"returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """returns printable representation of the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
