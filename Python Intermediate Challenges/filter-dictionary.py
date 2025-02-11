# Write a function to filter out non-integer values from a heterogeneous dictionary

def filter_dictionary(d):

    return {key: value for key, value in d.items() if isinstance(value, int)}

d = {'age': 25, 'name': 'Alice', 'height': 5.7, 'id': 101}
print(filter_dictionary(d))