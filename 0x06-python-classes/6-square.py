#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 2-square.py).
     """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter of the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of the attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter to the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the position"""
        if not isinstance((value, tuple) or len(value) != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square representation using #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + self.__size)
