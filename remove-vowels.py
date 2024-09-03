#Python program to remove all the vowels from a string.

def remove_vowels(string):

    vowels = 'A,E,I,O,U,a,e,i,o,u'

    new_str = ''

    for char in string:

        if char not in vowels:
            new_str += char
    print(new_str)

string = 'A quick brown fox jumps over the lazy dog'

remove_vowels(string)