#!/usr/bin/python3
"""Function that prints an element in a list at a specific index"""
def element_at(my_list, idx):
    if idx < 0:
         return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
