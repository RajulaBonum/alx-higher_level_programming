#!/usr/bin/python3
"""Function to append"""


def append_write(filename="", text=""):
    """a function that appends to the end of the UTF8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
