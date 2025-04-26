# Write a function to merge two dictionaries

def merge_two_dictionaries(dict1, dict2):

    return {**dict1, **dict2}

print(merge_two_dictionaries({'a':1, 'b':2}, {'c':3, 'd':4}))