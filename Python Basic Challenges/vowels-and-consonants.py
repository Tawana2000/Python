# Write a function to split a string into two parts: one containing all the vowels and the other containing all the consonants

def split_strings(s):

    vowels_container = 'AEIOUaeiou'
    vowels = ''
    consonants = ''

    for char in s:
        if char in vowels_container:
            vowels += char
        else:
            consonants += char

    return (vowels, consonants)

print(split_strings('hello'))