#!/usr/bin/pyhton3
"""Function that returns a list with all values multiplied by a number without using loops"""
def map_mul(my_list=[], number=0):
    mul_list = lambda a : a * number
    return list(map(mul_list, my_list))
