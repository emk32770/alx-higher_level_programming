#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list_direct = a_dictionary.copy()
    list_keys = list(list_direct.keys())

    for i in list_keys:
        list_direct[i] *= 2

    return (list_direct)
