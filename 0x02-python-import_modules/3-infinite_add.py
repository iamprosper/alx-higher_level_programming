#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    res = 0
    for i in range(1, args):
        res += int(sys.argv[i])
    print(res)
