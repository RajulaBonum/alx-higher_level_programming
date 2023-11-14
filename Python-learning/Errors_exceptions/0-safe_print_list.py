#!/usr/bin/python3
"""Function that prints x elements of a list"""
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
         for x in range(x):
             print(my_list[x],end=" ")
             count += 1
    except IndexError:
            pass
    print()
    return count
