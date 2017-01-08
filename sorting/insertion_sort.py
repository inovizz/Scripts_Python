#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

def insertionSort(myList):
    for i in range(1, len(myList)):
        print i
        for j in range(i-1, -1, -1):
            print j
            print myList[j], myList[j+1]
            if myList[j]>myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
                print myList
            else:
                continue

    return myList


a = [34, 56,11, 45, 0, 3, 99, 22, 66, 100, 5]

print insertionSort(a)
