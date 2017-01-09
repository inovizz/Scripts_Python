#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

import sys

def accend(lst):
    check = 0
    count = 0
    idx = 0
    for k in xrange(1,len(lst)):
        if lst[k] < lst[k-1] or (idx and lst[idx-1] and lst[k] < lst[idx-1]):
            count += 1
            idx = k-1
    if count > 1:
        print "False"
    elif count == 1:
        for k in xrange(idx-1,-1,-1):
            if lst[idx] > lst[k]:
                lst[idx], lst[k+1] = lst[k+1], lst[idx]
                break
        print "swapped"
    else:
        print "True" 


if __name__ == "__main__":
    accend(sys.argv[1])

# ----------------------------------------------------------------------------------

from itertools import combinations
def is_swappable(lst):
    s = sorted(lst)
    for i, j in combinations(range(len(lst)), 2):
        l = lst[:]
        l[i], l[j] = l[j], l[i]
        if l == s:
            return True
        else:
            return False