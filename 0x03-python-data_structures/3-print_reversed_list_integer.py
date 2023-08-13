#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    copy_list = my_list[:]
    my_list.reverse()
    for number in copy_list:
        print("{:d}".format(number))
