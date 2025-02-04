# Write a function to get all values of a dictionary

def get_values(dict):

    result = []

    for values in dict.values():
        result.append(values)

    return result

dict = {
    'a': 1,
    'b': 2, 
    'c': 3
}

print(get_values(dict))
