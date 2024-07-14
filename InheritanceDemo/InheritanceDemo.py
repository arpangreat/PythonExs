#!/usr/bin/env python3


class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


class B:
    def __init__(self):
        super().__init__()
        print("In B init")


class C(A, B):
    def __init__(self):
        super().__init__()
        # super(B).__init__()
        print("In C init")


# Method Resolution Order


# s1 = A()
# s2 = B()
s3 = C()
# s1.feature1()
# s1.feature2()
# s2.__init__()
# b1 = B()
# b1.feature2()
