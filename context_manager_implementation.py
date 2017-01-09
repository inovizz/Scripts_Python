#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for _ in range(10000):
    with File('fooo.txt', 'w') as infile:
        infile.write('fooo')
        files.append(infile)

