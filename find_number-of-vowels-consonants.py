#Given a non-empty string, find the total number of vowels and consonants present in the string.

def find_number(string):

    vowels = 'A,E,I,O,U,a,e,i,o,u'
    
    no_vowels = 0
    no_conso = 0

    for char in string:

        if char in vowels:
            no_vowels += 1
        elif char == ' ':
            continue
        else:
            no_conso += 1
    print('Number of vowels present in the string: ',no_vowels)
    print('Number of consonant present in the string: ',no_conso)


string = input('Enter the string: ')
find_number(string)