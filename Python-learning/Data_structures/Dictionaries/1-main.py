#!/usr/bin/python3
update_dict = __import__('1-update').update_dict
sort_dict =__import__('0-sort_dict').sort_dict

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dict(a_dictionary, 'languege', "Python")
sort_dict(new_dict)
print("--")
sort_dict(a_dictionary)

print("---")
print("---")

new_dict = update_dict(a_dictionary, 'city', "San Francisco")
sort_dict(a_dictionary)
print("--")
sort_dict(a_dictionary)
