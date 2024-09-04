#Create a Python program to count the number of capital letters in a string.
#In python we can use ord() to get the ASCII values

def capital(string):

    count = 0

    for char in string:

        if ord(char) >= 65 and ord(char) <= 90:
            count += 1

    print(count)


string = input('Enter the string to find the number of capital letters: ')
capital(string)