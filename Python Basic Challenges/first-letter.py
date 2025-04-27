# Write a function to find the first letter in a string that occurs only once

def single_occurence(s):

    for char in s:
        if s.count(char) == 1:
            return char
        
print(single_occurence('Hello World'))