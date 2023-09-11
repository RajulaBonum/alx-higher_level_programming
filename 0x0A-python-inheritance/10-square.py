#!/usr/bin/python3
"""class square inheriting from class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square attributes and methods"""

    def __init__(self, size):
        """private attribute"""
        self.__size = size
        super().__init__(self.__size, self.__size)
