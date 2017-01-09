#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

import csv, sys

def main(file1, file2):
    with open(file1, 'r') as f:
        r = csv.reader(f, delimiter=',')
        file_1 = []
        for i in r:
            file_1.append(i)

    with open(file2, 'r') as f:
        r = csv.reader(f, delimiter=',')
        file_2 = []
        for i in r:
            file_2.append(i)

    concat_list = []

    if len(file_1) >= len(file_2):
        for i in range(0, len(file_1)):
            try:
                x = file_1[i]
                y = file_2[i]
                concat_list.append(x + y)
            except IndexError:
                concat_list.append(file_1[i])
    else:
        for i in range(0, len(file_2)):
            try:
                x = file_2[i]
                y = file_1[i]
                concat_list.append(x + y)
            except IndexError:
                concat_list.append(file_2[i])
    return concat_list

def write_to_csv(main_func, output_file_name):
    for i in main_func:
        with open(output_file_name, 'ab') as f:
            wr =  csv.writer(f, delimiter=',')
            wr.writerow(i)

if __name__ == '__main__':
    write_to_csv(main(sys.argv[1], sys.argv[2]), sys.argv[3])