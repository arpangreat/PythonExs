#!/usr/bin/env python3


class Student:
    school = "R.J.L.V"

    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def avg(self):
        return (self.n1 + self.n2 + self.n3) / 3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class.. ")


s1 = Student(14, 34, 54)
s2 = Student(13, 56, 78)


print(s1.avg())
print(Student.getSchool())
Student.info()
