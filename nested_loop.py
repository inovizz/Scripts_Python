#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

a = [1,78, 67, 97, 0, 23, 67, 78]
max_diff = 0
in_po = 0
fi_po = 0


for i in a:
    for j in a:
        if a.index(i) < a.index(j) and j-i > max_diff:
            max_diff = j-i
            in_po = i
            fi_po = j

print max_diff
print in_po, fi_po