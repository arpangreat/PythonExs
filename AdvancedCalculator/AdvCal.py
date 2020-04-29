#!/usr/bin/env python3




def sum(a,b):
    return a + b


def sub(a,b):
    return a - b

def multi(a,b):
    return a * b

def divi(a,b):
    return a / b



class nor:


    def normalCalc(self):

        j = int(input("Enter your first value: "))
        k = int(input("Enter your Second value: "))
        print("Enter 1 for sum , 2 for substraction , 3 for multiply , 4 for dividation")
        i = int(input("Enter your choice: "))

        if i==1:
            print(sum(j,k))
        elif i==2:
            print(sub(j,k))
        elif i==3:
            print(multi(j,k))
        elif i==4:
            print(divi(j,k))

        else:
            print("Enter a valid option Please......")

c1 = nor()

class m2rc:


    def m2r(self):

        m2rl = [[0,0],[0,0]]
        m2rl[0][0] = int(input("Enter your Row1-Col1: "))
        m2rl[0][1] = int(input("Enter your Row1-Col2: "))
        m2rl[1][0] = int(input("Enter your Row2-Col1: "))
        m2rl[1][1] = int(input("Enter your Row2-Col2: "))

        i = int(input("Enter 1 to only show the matrix or 2 to determinante: "))

        if i==1:
            print("|" , m2rl[0][0] , m2rl[0][1] , "|")
            print("|" , m2rl[1][0] , m2rl[1][1] , "|")

        elif i==2:
            res1 = (m2rl[0][0]*m2rl[1][1])
            res2 = (m2rl[0][1]*m2rl[1][0])
            print("The value of determinante is : ", (res2 - res1))

        else:
            print("Enter a valid choice .....")

c2 = m2rc()


v = int(input("Enter 1 for normal calculator and 2 for 2/2 Matrix calculator and CTRL-C for Human Calculator: "))



if v==1:
    c1.normalCalc()

elif v==2:
    c2.m2r()

else:
    print("Please enter a valid choice .......")
