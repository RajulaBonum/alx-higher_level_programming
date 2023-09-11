#!/usr/bin/python3
"""Class rectangle that inherits from class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instatiation with width and height"""

    def __init__(self, width, height):
        """Both width and height are private instances attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
