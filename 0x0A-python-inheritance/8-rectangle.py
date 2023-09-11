#!/usr/bin/python3
"""Class rectangle that inherits from class BaseGeometry"""


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """instatiation with width and height"""

    def __init__(self, width, height):
        """Both width and height are private instances attributes"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
