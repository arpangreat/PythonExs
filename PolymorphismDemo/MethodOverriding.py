#!/usr/bin/env python3


class A:
    def show(self):
        print("In A Show")


class B(A):
    def show(self):
        print("In B Show")


a1 = B()
a1.show()
