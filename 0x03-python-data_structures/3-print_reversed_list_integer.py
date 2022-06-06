#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # i = -1
    # list_size = -(len(my_list))
    # while (i >= list_size):
    #    print("{:d}".format(my_list[i]))
    #    i += -1
    my_list.reverse()
    for element in my_list:
        print("{:d}".format(element))
