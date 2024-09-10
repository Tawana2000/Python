#Create a Python program to print the character that repeats itself in a subsequent sequence, for ex: 'hello' the program should return l.

def sub(string):

    for i in range (len(string)):

        if string[i] == string[i + 1]:
            return string[i]
        
string = 'hello'
print(sub(string))