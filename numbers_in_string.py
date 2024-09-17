#Write a Python program to count the number of digits in a string.

def count(string):

    number = '0123456789'
    count = 0

    for num in string:
        if num in number:
            count += 1

    return count

string = input()
print(count(string))
