# Write a program to create a class and print attributes using a method of the class.

class Bicycle:
    def __init__(self,gear,speed):
        self.gear = gear
        self.speed = speed

    def print_value (self):
        print(self.gear)
        print(self.speed)

bicycle = Bicycle(4,80)
bicycle.print_value()