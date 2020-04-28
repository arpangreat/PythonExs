import sys
a = int(input('Enter Your First Value:'))
b = int(input('Enter Your Second Value:'))

if not( a > b or a == b ):
    print("a is greater than b")
elif not( a < b  and a == b):
    print("a is greater than b")
else:
    print("b is greater than a")
