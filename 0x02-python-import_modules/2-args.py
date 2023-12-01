#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv)
    if x == 1:
        print("{} arguments.".format(x - 1))
    elif x == 2:
        print("{} argument:".format(x - 1))
    else:
        print("{} arguments:".format(x - 1))

    for i in range(1, x):
        print("{}: {}".format(i, sys.argv[i]))
