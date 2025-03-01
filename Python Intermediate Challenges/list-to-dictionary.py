# Write a function to convert two lists into a dictionary

def lists_to_dict(list1, list2):

    return dict(zip(list1, list2))

list1 = ['d', 'e', 'f']
list2 = [4, 5, 6]

print(lists_to_dict(list1, list2))