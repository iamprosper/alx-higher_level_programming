#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for item in sorted_dict:
        print("{}: {}".format(item, a_dictionary.get(item)))
