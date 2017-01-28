#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

obj = Stack()
obj.push(5)
obj.push(6)
obj.push(7)
obj.push(8)
obj.push(9)
obj.push('addfg')
print obj.isEmpty()
print obj.peek()
print obj.size()
obj.pop()
print obj.size()