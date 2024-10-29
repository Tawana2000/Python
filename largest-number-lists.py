# Write a function to find the largest number in each list from a group of lists

def find_largest(lst):

    largest_numbers = [max(sublist) for sublist in lst]

    return largest_numbers


lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(find_largest(lst))

