#Create a Python program to find the length of the last word in a string.

def length(string):

    new_str = string.split(' ')
    l = len(new_str[-1])
    if new_str[-1].endswith('.'): #not counting the punctuation
        l -= 1
    print(l)
string = 'I love Programming.'
length(string)