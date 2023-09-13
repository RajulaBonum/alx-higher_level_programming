#!/usr/bin/python3
"""Defines a function that add attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute (att) to an object (obj)
    The value of the attribute is (value)
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
