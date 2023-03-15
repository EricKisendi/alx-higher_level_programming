#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = {}
    keys1 =list(a_dictionary.keys())
    keys1.sort()
    for i in keys1:
        b_dictionary[i] = a_dictionary.get(i)
    print(b_dictionary)
