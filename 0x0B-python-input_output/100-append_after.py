#!/usr/bin/python3
"""function that inserts a line of text to a file, after each line"""


def append_after(filename="", search_string="", new_string=""):
    """module search and update"""
    text = ""
    with open(filename, 'r') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
