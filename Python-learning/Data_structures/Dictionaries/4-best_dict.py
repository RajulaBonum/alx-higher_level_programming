#!/usr/bin/python3

def best_dict(a_dictionary):
    if a_dictionary:
        maximum = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == maximum:
                best_s = key
        return best_s
    else:
        return None
