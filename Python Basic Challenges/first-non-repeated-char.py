# Write a function to find and return the first non-repeated character in a string

def first_nonrepeated(s):

    for char in s:
        if s.count(char) == 1:
            return char

print(first_nonrepeated('bubble'))