#Write a program to create a function that can take a variable number of arguments and returns the product of numbers passed as arguments.

def product(n1,n2,n3):
    result  = n1 * n2 * n3
    print(result)
n1 = int(input())
n2 = int(input())
n3 = int(input())

product(n1,n2,n3)