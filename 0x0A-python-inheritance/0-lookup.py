#!/usr/bin/python3
"""function to get the attributes and methods of an object using dir()"""

def lookup(object):
    return [att for att in dir(att) if callable(getatt(object, att))]
