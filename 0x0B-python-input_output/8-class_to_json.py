#!/usr/bin/python3
"""function that returns the dictionary description with simple data"""


def class_to_json(obj):
    """returns builds a dictionary"""
    return obj.__dict__
