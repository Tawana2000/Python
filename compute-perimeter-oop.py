#Program to compute the perimeter of a triangle using OOP.

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        self.p = self.a + self.b + self.c
        print(self.p)

    #def result(self):
        #print(self.c)

a = int(input())
b = int(input())
c = int(input())

tri = Triangle(a,b,c)
tri.add()
#tri.result()