# Write a function to count the number of occurrence of each letter in a given word. 

def count_letter(word):

    result = {}
    for char in word:
        result[char] = result.get(char, 0) + 1
    return result

print(count_letter('apple'))


"""
#To make it more efficient 

from collections import Counter

def count_letter(word):

    return dict(Counter(word))

print(count_letter('apple'))

"""