#!/usr/bin/python3
new_in = __import__('4-new_in_list').new_in

my_list = [1, 2, 3, 4, 5]
idx = 3
element = 9
new = new_in(my_list, idx, element)

print("Original", my_list)
print("new", new)
