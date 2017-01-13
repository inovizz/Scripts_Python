#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
__author__ = "Sanchit"

def main(n):
    hex_dict = {"A": 10, "B":11, "C":12, "D":13, "E":14, "F":15}
    counter = len(n)-1
    res = 0
    for i in n:
        try:
            a = int(i)
            res+=(16**counter)*a
        except:
            res+=(16**counter)*(hex_dict[i])
        counter-=1
    return res


if __name__ == '__main__':
    print main(sys.argv[1])
    print main("1C7")
    print main("FF")
    print main("DD")
