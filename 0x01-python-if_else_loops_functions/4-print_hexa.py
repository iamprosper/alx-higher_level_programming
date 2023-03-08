#!/usr/bin/python3
for i in range(99):
    print("{} = {}".format(i, "0x"), end="")
    if (i < 10):
        print("{}".format(i))
    elif (i < 16):
        print("{}".format(chr(i + 87)))
    elif (i % 16 == 0):
        print("{}0".format(i // 16))
    else:
        print("{:d}".format(i // 16), end="")
        if (i % 16 >= 10):
            print("{}".format(chr((i % 16 + 87))))
        else:
            print("{}".format(i % 16))
