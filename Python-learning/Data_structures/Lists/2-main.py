#!/usr/bin/python3
replace_in = __import__('2-replace').replace_in

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in(my_list, idx, new_element)

print(new_list)
print(my_list)
