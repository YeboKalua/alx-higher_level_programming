#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    our_list = []
    try:
        new_list = my_list[:x]
        for item in new_list:
            our_list.append(item)
            count += 1
        our_list.append("\n")
        for element in our_list:
            print(element, end="")
        return count
    except IndexError:
        x = count
