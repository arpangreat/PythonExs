#!/usr/bin/env python3
i = input("Enter your name")
j = input("Enter your os")

class Computer:

    def __init__(self,a,b):
        self.a = a
        self.b = b

        print(f"this is {a}'s  {b} machiene ")

    def config(self):
        print("This machiene")


com1 = Computer(i,j)
com1.config()

print(type(com1))
