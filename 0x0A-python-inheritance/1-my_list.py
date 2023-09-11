#!/usr/bin/python3
"""Class MyList that inherits from class list"""


class MyList(list):
    """public instance method to print list in sorted format"""
    def print_sorted(self):
        """instance to print sorted list"""
        sortlist = sorted(self)
        print(sortlist)
