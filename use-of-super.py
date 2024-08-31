#program that calls a method of the base class from inside a method of a derived class using the

class Animal:

    def eat(self):
        print('I can eat food')

class Dog(Animal):
    def bark(self):
        print('I can bark')
        super().eat()

d1 = Dog()
d1.bark()