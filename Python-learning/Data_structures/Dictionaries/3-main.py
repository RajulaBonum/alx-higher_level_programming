#!/usr/bin/python3
del_dict = __import__('3-del_dict').del_dict
sort_dict = __import__('0-sort_dict').sort_dict

a_dictionary = { 'language': "C", 'Number': 89, 'track': "low", 'ids': [1, 2, 3]}
new_dict = del_dict(a_dictionary, 'track')
sort_dict(a_dictionary)
print("--")
sort_dict(new_dict)

print("--")
print("--")
new_dict = del_dict(a_dictionary, 'c_is_fun')
sort_dict(a_dictionary)
print("--")
sort_dict(new_dict)
