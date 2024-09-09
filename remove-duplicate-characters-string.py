#Create a Python program to remove duplicate characters from a string.

def remove(string):

    new_str = ''

    for char in string:
        if char not in new_str:
            new_str += char

    print(new_str)

string = '12star23'
remove(string)

        