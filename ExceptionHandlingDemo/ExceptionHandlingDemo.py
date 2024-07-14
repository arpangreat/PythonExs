#!/usr/bin/env

a = int(input("Enter the first num: "))
# b = 3
b = int(input("Enter the second num: "))

try:
    print("Resource open")
    print(a / b)

# except Exception:
#   print("Hey you cannot divide by Zero")

# Printing the exception message too
except ZeroDivisonError as e:
    print("Hey ,you cannot divide by Zero !!!", e)

finally:
    print("Resourece closed")

print("Bye")
