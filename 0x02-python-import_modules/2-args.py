#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    print("{:d} argument".format(args - 1), end="")
    if (args > 1):
        if (args > 2):
            print("s", end="")
        print(":")
        for i in range(1, args):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("s.")
