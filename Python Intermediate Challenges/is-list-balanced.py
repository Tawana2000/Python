# Write a function to check if a list is balanced or not

def is_balanced(lst):

    half = len(lst) // 2
    return sum(lst[:half]) == sum(lst[-half:])

print(is_balanced([1, 2, 3, 3, 2, 1]))