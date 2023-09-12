#!/usr/bin/python3
"""function to read a text from file"""


def read_file(filename=""):
    """opens and reads contents of a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
