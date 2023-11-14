#!/usr/bin/python3
"""Function that replaces an element in a list with a new one"""
def replace_in(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
