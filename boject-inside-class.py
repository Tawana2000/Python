#Write a program to create an object of one class inside another class.

class Engine:
    def __init__(self,power):
        self.power = power


class Vehicle:
    def __init__(self,wheels,engine):
        self.wheels = wheels
        self.engine = Engine(400)
    
    def get_power(self):
        print(self.engine.power)

v1 = Vehicle(4,400)
v1.get_power()