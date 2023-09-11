#!/usr/bin/python3
"""class Basegeometry"""


class BaseGeometry:
    """Public instance method area"""
    def area(self):
        raise Exeception("area() is not implemented")

    """public instance method integer_validator"""
    def integer_validator(self, name, value):
        """validate name attribute"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
