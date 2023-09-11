#!/usr/bin/python3
"""Func to check inheritance"""


def inherits_from(obj, a_class):
    """use of function type and isinstance to determine inheritance"""
    return type(obj) != a_class and isinstance(obj, a_class)
