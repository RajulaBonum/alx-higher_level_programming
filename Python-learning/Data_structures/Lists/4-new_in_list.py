#!/usr/bin/python3
"""Function that replaces an element in a copy of the original"""
def new_in(my_list, idx, element):
    new = my_list[:]
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        new[idx] = element
        return new
