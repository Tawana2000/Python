# Write a program to remove every vowel from a given string

def rmv_vowel(string):
    
    vowel = 'aeiouAEIOU'
    result = ''.join([char for char in string if char not in vowel])
    return result


string = 'Hello World'
print(rmv_vowel(string))