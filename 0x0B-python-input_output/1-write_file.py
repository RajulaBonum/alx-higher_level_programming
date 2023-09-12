#!/usr/bin/python3
"""Function to write a string to a text file UTF8"""


def write_file(filename="", text=""):
    """writes into a file"""
    with open(filename, 'w') as f:
        return f.write(text)
