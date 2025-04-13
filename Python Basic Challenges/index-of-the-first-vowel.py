# Write a function to find the index of the first vowel in a given string
def first_vowel_index(s):

    vowel = 'AEIOUaeiou'

    for char in s:
        if char in vowel:
            result =  s.index(char)
            return result
    
print(first_vowel_index('Hello'))