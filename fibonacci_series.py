#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"


# ------------------ using generator function ----------------------
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

# ---------------------- using recursion -----------------------------
print "\n"

def fibonacci_recursion(num):
    import pdb; pdb.set_trace()
    if num <2:
        return num
    else:
        return fibonacci_recursion(num - 1) + fibonacci_recursion(num-2)

for i in range(0, 11):
    print fibonacci_recursion(i),