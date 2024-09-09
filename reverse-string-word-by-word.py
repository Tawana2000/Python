#Create a Python program to reverse a string word by word.

def rev(string):

    new_str = string.split(' ')
    new_str_rev = new_str[::-1]
    result = ' '.join(new_str_rev)
    print(result)

string = 'this is blue'
rev(string)