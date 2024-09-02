#Write a Python program to reverse a list of size n and print it.

def rev(l1):

    l2 = l1[::-1]
    print(l2)

l1 = [5, 8, 4, 7, 1, 23, 6]
rev(l1)