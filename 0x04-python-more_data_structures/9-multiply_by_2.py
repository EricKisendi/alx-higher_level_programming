#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    new_values = list(new_dictionary.values())
    new_list = []
    new_keys = list(new_dictionary.keys())
    for i in new_values:
        new_list.append(i*2)
    for x in range(len(new_list)):
        print("{}: {}".format(new_keys[x], new_list[x]))
