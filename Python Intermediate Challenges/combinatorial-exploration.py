# Write a function to generate all possible combinations of a given list of items

import itertools
def generate_combinations(lst):

    return [comb for r in range(1, len(lst) + 1) for comb in itertools.combinations(lst, r)]

print(generate_combinations([1, 2, 3]))