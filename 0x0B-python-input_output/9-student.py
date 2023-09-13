#!/usr/bin/python3
"""class student
"""


class Student:
    """student class """

    def __init__(self, first_name, last_name, age):
        """method to initialize attributes 
        """
        self.first_name = first_name
        self.first_name = last_name
        self.age = age

    def to_json(self):
        """method to_json
        """
        return self.__dict__
