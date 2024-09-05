#Create a Python program to add any number of parameters in a function.

def add(*args):

    sum = 0

    for num in args:
        sum += num

    print(sum)

add(12,3,10,7)