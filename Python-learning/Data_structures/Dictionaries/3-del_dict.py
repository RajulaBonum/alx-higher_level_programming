#!/usr/bin/python3
"""Function that deletes a key from a dictionary"""
def del_dict(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
