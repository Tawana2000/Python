# Write a function to check if two sets have any elements in common. If yes, display the common elements 

def common_elements(set1, set2):

    result = {num for num in set1 if num in set2}
    return result if result else None

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(common_elements(set1, set2))