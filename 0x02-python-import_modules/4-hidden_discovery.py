#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import *
    name = dir()
    for i in range(len(name)):
        if name[i][:2] != '__':
            print("{}".format(name[i]))
