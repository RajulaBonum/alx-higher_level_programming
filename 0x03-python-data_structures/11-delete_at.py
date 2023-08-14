#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new = []
    for i, j in my_list:
        if i != idx:
            new.append(j)
    return new
