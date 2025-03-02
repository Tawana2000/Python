# Write a function to generate all n-size combinations from a given list 

from itertools import combinations
def generate_combinations(lst, n):

    return list(combinations(lst, n))

print(generate_combinations([1, 2, 3, 4], 2))