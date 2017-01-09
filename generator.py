#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

# ---------------- generator example to print fibonacci series --------------
def fibonacci(limit):
    count = 0
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
        if (count == limit):
            break
        count += 1

for n in fibonacci(10):
    print n,

#-------------------Generator function to generate iterators -------------
def gen_interator(start=0, limit=0):
    if start is None:
        start = 0
    i = start
    while i<= limit:
        yield i
        i+=1

a=  gen_interator(0,5)

print a.next()
print a.next()
print a.next()
print a.next()
print a.next()

