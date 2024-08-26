#Write a program to create a class that will have a method that returns the sum of a student's scores stored in a list.

class Student:

    def __init__(self,score):
        self.score = score

    def get_sum(self):
        self.Sum = sum(self.score)
        print(self.Sum)
        

score = [55,75,80,62,77]

s1 = Student(score)
s1.get_sum()