# Write a function to flatten a nested list iterator

def flatten_nested_list(nested_list):

    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))

        else:
            result.append(item)
    return result

nested_list = [[1, 1], 2, [1, 1]]
print(flatten_nested_list(nested_list))