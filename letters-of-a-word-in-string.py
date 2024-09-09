#Create a Python program to check if all the characters in a string are contained in a list.


def letters(list1,string):

    for char in string:
        if char not in list1:
            return False
    return True

list1 = ['a', 'l', 'p', 'c', 'e', 'd']
string = 'apple'

print(letters(list1, string))