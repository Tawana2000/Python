# Write a function to generate all permutations of a given list.

from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))


print(generate_permutations([1, 2, 3]))
