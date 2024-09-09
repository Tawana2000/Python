#Create a Python program to count the alphabets, digits, and symbols in a string.


def count(string):

    alphabets = 0
    digits = 0
    symbols = 0

    for items in string:

        if items.isalpha():
            alphabets += 1
        elif items.isdigit():
            digits += 1
        else:
            symbols += 0

    print('Alphabets:',alphabets)
    print('Digits:',digits)
    print('Symbols:',symbols)

string = 'hello123.'
count(string)