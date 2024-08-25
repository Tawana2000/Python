#Write a program to create a function that can take a variable number of keyword arguments.
#Expected output : {'first': 'Joe', 'last': 'Biden'}

def name(**args): #** receives arguments as a dictionary
    print(args)

first = input()
last = input()

name (first=first , last=last)