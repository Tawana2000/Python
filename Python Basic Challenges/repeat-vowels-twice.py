# Write a function to repeat all vowels twice in a given string

def repeat_vowels(string):

    vowels = 'AEIOUaeiou'
    new_str = ''
    
    for char in string:
        new_str += char
        if char in vowels:
            new_str += char
    return new_str

print(repeat_vowels('hello'))
print(repeat_vowels('Breakfast'))
