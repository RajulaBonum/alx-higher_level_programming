#!/usr/bin/python3
common_elem = __import__('0-common').common_elem

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elem(set_1, set_2)
print(sorted(list(c_set)))
