#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for int in (my_list[::-1]):
        print("{:d}".format(int))
