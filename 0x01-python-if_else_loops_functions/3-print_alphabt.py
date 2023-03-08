#!/usr/bin/python3
i = 97
for i in range(i, 123):
    if (chr(i) != 'q' and chr(i) != 'e'):
        print("{}".format(chr(i)), end="")
