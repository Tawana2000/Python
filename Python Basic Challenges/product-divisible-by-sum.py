# Write a funtion to check if the product of all numbers in a list is divisible by the sum of those numbers.

def is_divisible(numbers):
    
    product = 1

    for i in numbers:
        product *= i

    return True if product % sum(numbers) == 0 else False

print(is_divisible([2, 3, 4]))