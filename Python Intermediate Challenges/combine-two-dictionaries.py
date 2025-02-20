# Write a function to combine two dictionaries into one

def combine_dictionaries(dict1, dict2):

    return dict1 | dict2

dict1 = {'e': 5, 'f': 6}
dict2 = {'g': 7, 'h': 8}

print(combine_dictionaries(dict1, dict2))

