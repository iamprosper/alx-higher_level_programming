#!/usr/bin/python3
def odd_even(number):
    if (number % 2 == 0):
        return True
    return False


for i in range(122, 96, -1):
    if odd_even(i):
        pass
    else:
        i -= 32
    print("{}".format(chr(i)), end="")
    if not odd_even(i):
        i += 32
