#!/usr/bin/python3
"""Class square"""

class Square:
    """
    Attributes
    """
    def __init__(self, size=0):
        """
        Create new instance of square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
