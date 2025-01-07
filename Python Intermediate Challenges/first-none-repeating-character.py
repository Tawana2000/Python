# Write a program to find the first none repeating character in a string

from collections import Counter

def first_non_repeating_char(s):
    char_count = Counter(s)
    for char in s:
        if char_count[char] == 1:
            return char
    return None

s = "swiss"
print(first_non_repeating_char(s))
