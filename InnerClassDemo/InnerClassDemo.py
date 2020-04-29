#!/usr/bin/env python3

class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name , self.roll)



    class Laptop:
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = '4 GB'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Swastik',3)


s1.show()

s1.lap.show()
