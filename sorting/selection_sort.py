#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

def selectionSort(myList):
    for i in xrange(0, len(myList)-1):
        minIndex = i
        for j in xrange(i+1, len(myList)):
            if myList[j] < myList[minIndex]:
                minIndex = j
        if minIndex != i:
            myList[i], myList[minIndex] = myList[minIndex], myList[i]

    return myList

a = [34, 56,11, 45, 0, 3, 99, 22, 66, 100, 5]

print selectionSort(a)