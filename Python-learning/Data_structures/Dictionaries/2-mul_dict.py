#!/usr/bin/python3
"""Funtion that multiplies the values of a dictionary by 2"""
def mul_dict(a_dictionary):
    for key, value in a_dictionary.items():
        a_dictionary[key] = value * 2
    return a_dictionary
