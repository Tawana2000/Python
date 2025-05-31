#Create a program to call the method of the base class using an object of the derived class.

class Animal:
    def eat(self):
        print('I can eat')

class Dog(Animal):
    def bark(self):
        print('I can bark')

d = Dog()
d.eat()
