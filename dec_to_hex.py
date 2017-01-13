#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
__author__ = "Sanchit"

def convert_dec_to_hex(n):
    if n % 16 == 10:
        x = 'A'
    elif n % 16 == 11:
        x = 'B'
    elif n % 16 == 12:
        x = 'C'
    elif n % 16 == 13:
        x = 'D'
    elif n % 16 == 14:
        x = 'E'
    elif n % 16 == 15:
        x = 'F'
    else:
        x = n % 16
    return x

def main(n):
    n = int(n)
    if n < 16:
        return convert_dec_to_hex(n)
    else:
        rem = n % 16
        div = n/16
        return str(main(div)) + str(convert_dec_to_hex(rem))

if __name__ == '__main__':
    print main(sys.argv[1])
