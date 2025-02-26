# Write a function to calculate the standard deviation of a list of numbers

import math

def calculate_std_dev(numbers):

    if not numbers:
        raise ValueError("List cannot be empty")
    
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return round(math.sqrt(variance), 2)


print(calculate_std_dev([2, 4, 4, 4, 5, 5, 7, 9]))
print(calculate_std_dev([1, 2, 3, 4, 5]))         
print(calculate_std_dev([10]))