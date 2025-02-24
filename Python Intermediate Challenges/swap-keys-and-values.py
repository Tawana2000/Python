# Write a function to swap keys and values in dictionary 

def swap_dictionary(dict):

    return {v: k for k, v in dict.items()}

print(swap_dictionary({'a': 3, 'b': 21, 'c': 11}))