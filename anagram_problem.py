#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"
from collections import Counter
# find if two given strings are anagram, using Counter method of collections data structure
# This implementation is just similar to creating a dictionary out of a string and
# increasing the counter whenever the word occurs again in string.
# In the end we can match both dictionaries, if they are equal then both strings
# will be considered as anagram of each other, otherwise not.

def checkAnagram(s1, s2):
    if not isinstance(s1, str) and not isinstance(s2, str):
        print "Given inputs are incorrect"
    else:
        if len(s1) != len(s2):
            print "Given strings are not anagrams of each other"
        else:
            if Counter(s1) == Counter(s2):
                print "Given strings are anagram of each other"
            else:
                print "Given strings are not anagrams of each other"

print checkAnagram("Geekforgeeks", "forgeekgeeks")
print checkAnagram(0,1)

# Solution to hackerrank anagram problem
# Problem statement - https://www.hackerrank.com/challenges/ctci-making-anagrams

def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum([abs(i) for i in ct_a.values()])

# a = raw_input().strip()
# b = raw_input().strip()
a = "cde"
b = "abc"

print number_needed(a, b)

