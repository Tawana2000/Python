#program to compute the area and perimeter of a square using class.

class square:

    def __init__(self,a):
        self.a = a

    def compute(self):

        self.area = self.a * self.a
        self.perimeter = self.a + self.a + self.a + self.a

        print(self.area)
        print(self.perimeter)

a = int(input())

s = square(a)
s.compute()