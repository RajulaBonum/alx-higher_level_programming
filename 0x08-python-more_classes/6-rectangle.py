#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    """public class attribute"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter the width of the Rectangle."""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if sel.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if sel.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__height + self.__width) * 2

    def __str__(self):
        """method: __str__
        return: nice string representation of rectangle
        """
        rect = []
        if self.__height == 0 or self.__width == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')
            if i != self.__height:
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """method: __repr__
        return: representation of rectangle that can be used by eval() to
        create new object
        """
        rect = "Rectangle(" + str(self.__width) + ","
        rect += str(self.__height) + ")"
        return rect

    def __del__(self):
        """method: __del__
        deletes instance of Rectangle class, and prints "bye" message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
