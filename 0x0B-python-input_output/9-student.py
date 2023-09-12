#!/usr/bin/python3
"""class student
"""


class Student:
    """student class """

    def __init__(self, first_name, last_name, age):
        """method __int__
        """
        self.firstname = first_name
        self.firstname = last_name
        self.age = age

    def to_json(self):
        """method to_json
        """
        return self.__dict__
