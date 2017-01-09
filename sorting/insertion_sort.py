#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

def insertionSort(alist):
   for index in range(1,len(alist)):
       currentvalue = alist[index]
       position = index
       while position>0 and alist[position-1]>currentvalue:
           alist[position]=alist[position-1]
           position = position-1
           alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


# def insertionSort(myList):
#     for i in range(1, len(myList)):
#         print i
#         for j in range(i-1, -1, -1):
#             print j
#             print myList[j], myList[j+1]
#             if myList[j]>myList[j+1]:
#                 myList[j], myList[j+1] = myList[j+1], myList[j]
#                 print myList
#             else:
#                 continue
#
#     return myList
#
#
# a = [34, 56,11, 45, 0, 3, 99, 22, 66, 100, 5]
#
# print insertionSort(a)
