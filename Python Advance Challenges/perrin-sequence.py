# Write a function that generates the Perrin sequence and returns the nth Perrin number.
# The Perrin sequence is an integer sequence where each number is the sum of the previous two numbers, starting with 3, 0, and 2
# For n > 2, t(n) = t(n - 2) + t(n - 3)

def perrin(n):

    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    
    else:
        return perrin(n - 2) + perrin(n - 3)
    
print(perrin(5))