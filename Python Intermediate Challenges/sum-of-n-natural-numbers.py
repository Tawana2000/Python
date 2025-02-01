# Write a function to find the sum of n natural numbers

def sum_natural_numbers(n):
    
    result = 0

    for i in range(1, n + 1):

        result += i
    
    return result

print(sum_natural_numbers(5))