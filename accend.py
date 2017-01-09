#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"


def swap(lst):
    count = 0
    for k in range(0, len(lst)-1):
        if lst[k] > lst[k+1]:
            count += 1
    if int(count) == 2:
        print "Swapped"
    elif int(count) == 0:
        print True
    else:
        print False


if __name__ == "__main__":
    swap([1,2,3,4,0])
    swap([6,4,2,5])
    swap([6,4,2,8])
    swap([1,2,3,4])

