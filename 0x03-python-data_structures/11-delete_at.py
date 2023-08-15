#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new = []
    i = 0
    while i < len(my_list):
        if i != idx:
            new.append(my_list[i])
        i+= 1
    my_list[:] = []
    i = 0
    while i < len(new):
        my_list.append(new[i])
        i+= 1
    return new
