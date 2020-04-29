#!/usr/bin/env python3

s = 5

s = 'Swastik'

class Emacs:

    def execute(self):
        print("Compiling")
        print("Running")


class Arpanemacs:

    def execute(self):
        print("My ide comes with all things")
        print("And many other")




class Laptop:

    def code(self, ide):
        ide.execute()


#ide = Emacs()
ide = Arpanemacs()

lap1 = Laptop()
lap1.code(ide)
