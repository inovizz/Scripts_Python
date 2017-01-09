#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

import time

def timetest(input_func):

    def timed(*args, **kwargs):

        start_time = time.time()
        result = input_func(*args, **kwargs)
        print args
        print kwargs
        end_time = time.time()
        print "Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
            input_func.__name__,
            args,
            kwargs,
            end_time - start_time
        )
        print result
    return timed


@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print "inside foobar"
    print args, kwargs


foobar(1,2,3,4, a=9, b=7)

#------------------------------ Another basic example-----------------------------------
def debug(f):            # debug decorator takes function f as parameter
    msg = f.__name__     # debug message to print later
    def wrapper(*args):  # wrapper function takes function f's parameters
        exec_time=  time.time()
        print msg, exec_time     # print debug message or do something before executing that function
        res =  f(*args)  # call to original function
        return res
    return wrapper       # return the wrapper function, without calling it

@debug
def mul(x):
    return x**2

@debug
def div(x, y):
    return x / y

print mul(2)
print div(4,2)
