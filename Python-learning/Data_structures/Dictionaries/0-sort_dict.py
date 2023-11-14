#!/usr/bin/python3
"""print sorted keys"""
def sort_dict(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(key, ":", value)
