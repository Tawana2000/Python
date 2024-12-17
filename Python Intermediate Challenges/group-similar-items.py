# Write a function to group similar items from a list into a dictionary 
# Return a dictionary where the keys are the items and the values are lists of indices where the items are found in the original list

def group_items(items):

    result = {}
    for index, item in enumerate(items):
        if item not in result:
            result[item] = []  # Initialize a list for the item if not already present
        result[item].append(index)  # Append the current index to the list
    return result

# Example Usage
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
grouped_indices = group_items(items)
print(grouped_indices)
