#Create a Python program to display the indexes of uppercase letters in a string.

def upper_case(string):

    upper = []

    for index, char in enumerate(string):
        if char.isupper():
            upper.append(index)
    return upper

string = 'heLLo'
print(upper_case(string))