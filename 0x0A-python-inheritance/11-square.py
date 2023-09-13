#!/usr/bin/python3
"""
class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""class square"""


class Square(Rectangle):
    """inside class square"""
    def __init__(self, size):
        """initializing size of square"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """str function"""
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
