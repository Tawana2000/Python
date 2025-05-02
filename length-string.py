#program to count the length of the string without using the len() function.

def length(string):

    count = 0

    for char in string:
        count += 1
    print(count)

string = input()
length(string)
