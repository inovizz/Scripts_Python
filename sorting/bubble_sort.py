#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

def bubbleSort(myList):
    for i in xrange(0, len(myList)-1):
        for j in xrange(0, len(myList)-1-i):
            print myList[j], myList[j+1]
            if myList[j]>myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList

a = [34, 56,11, 45, 0, 3, 99, 22, 66, 100, 5]

print bubbleSort(a)
