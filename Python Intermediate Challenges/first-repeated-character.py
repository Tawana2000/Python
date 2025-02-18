# Write a function to find the character that repeats first in the string

def first_repeating_char(s):

    present = set()

    for char in s:

        if char in present:
            return char
        
        present.add(char)

    return None

print(first_repeating_char('hello'))

