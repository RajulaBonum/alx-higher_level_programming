#!/usr/bin/python3
"""class student
"""


class Student:
    """student class """

    def __init__(self, first_name, last_name, age):
        """method __int__
        """
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get the dictionary representation of the student
        if attr is a list of strings
        """
        if (is(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
