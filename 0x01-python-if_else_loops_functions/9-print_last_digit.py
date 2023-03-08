#!/usr/bin/python3
def print_last_digit(number):
    str_n = int(str(number)[-1])
    print("{}".format(str_n), end="")
    return str_n

# print("{}".format(print_last_digit(98)))
# print("{}".format(print_last_digit("Holberton")))
# print("{}".format(print_last_digit(-1024)))
