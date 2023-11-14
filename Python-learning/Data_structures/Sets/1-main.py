#!/usr/bin/python3
unique_elem = __import__('1-unique').unique_elem

set_1 = { "Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
od_set = unique_elem(set_1, set_2)
print(sorted(list(od_set)))
