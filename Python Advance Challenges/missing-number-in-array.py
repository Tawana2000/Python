# Given an array containing n distinct numbers taken from the range 1 to n + 1, find the missing number.

def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    return total_sum - array_sum

print(find_missing_number([1, 2, 4, 5, 6]))
