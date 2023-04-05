#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_srt = list(a_dictionary.keys())
    list_srt.sort()
    for x in list_srt:
        print("{}: {}".format(x, a_dictionary.get(x)))
