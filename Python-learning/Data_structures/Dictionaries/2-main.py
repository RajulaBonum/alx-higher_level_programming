#!/usr/bin/python3
mul_dict = __import__('2-mul_dict').mul_dict
sort_dict = __import__('0-sort_dict').sort_dict

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = mul_dict(a_dictionary)
sort_dict(a_dictionary)
print("--")
sort_dict(new_dict)
