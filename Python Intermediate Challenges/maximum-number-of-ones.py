# Write a function to calculate the maximum number of ones

def calculate_numbers(n):

    return {
        'ones': n,
        'threes': n // 3,
        'nines': n // 9
    }

print(calculate_numbers(10))

    