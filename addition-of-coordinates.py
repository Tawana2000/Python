#Create a program to find the sum of two coordinates by creating objects.

class Coordinate():
    def __init__(self,a1,b1,a2,b2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2

    def sum(self):
        self.c1 = self.a1 + self.a2
        self.c2 = self.b1 + self.b2

    def result(self):
        print(self.c1)
        print(self.c2)
co = Coordinate(5,6,7,9)
co.sum()
co.result()
