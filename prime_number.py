#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"


def get_prime_numbers(limit):
    my_list = []
    numbr = ""
    for num in range(1, limit):
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            my_list.append(num)
            numbr+=str(num)+","
    # return numbr.rstrip()
    return my_list

print get_prime_numbers(101)
