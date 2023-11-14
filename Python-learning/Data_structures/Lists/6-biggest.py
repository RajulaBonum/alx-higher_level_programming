#!/usr/bin/python3
"""Function that returns the biggest integer of a list"""
def big_int(my_list=[]):
    if my_list == ():
        return None
    else:
        my_list.sort()
        length = len(my_list)
        return my_list[length - 1]
