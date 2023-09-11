#!/usr/bin/python3
"""function to determine subclasses"""


def is_same_class(obj, a_class):
    """returns true if the object is a subclass of a_class"""
    return type(obj) is a_class
