#!/usr/bin/python3
"""Function that prints list in reverse"""
def reverse_list(my_list=[]):
    new = []
    for i in range(len(my_list)):
        new.append(my_list[-i-1])
    return new
