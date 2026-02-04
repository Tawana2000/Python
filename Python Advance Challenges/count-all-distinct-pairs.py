# Write a function to count all distinct pairs in an list with difference equal to k

def count_pairs(numbers, k):

    numbers_set = set(numbers)
    count = sum(1 for numbers in numbers_set if numbers + k in numbers_set)
    return count
print(count_pairs([1, 5, 3, 4, 2], 2))
