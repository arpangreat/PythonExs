#!/usr/bin/env python3
#
#
# Doesn't Support in Python so we have to go with some checks


class Student:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c

        elif a != None and b != None:
            s = a + b

        else:
            s = a

        return s


s1 = Student(78, 90)

print(s1.sum(34, 45, 34))
print(s1.sum(34, 45))
print(s1.sum(34))
