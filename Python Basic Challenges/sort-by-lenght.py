# Write a function to sort a list of strings by their lenght.

def sort_by_length(lst):

    return sorted(lst, key = len)

print(sort_by_length(['apple', 'cherry', 'date']))
        