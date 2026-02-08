# Write a function to calculate the maximum value using '+' or '*' sign between two numbers in a string

def max_value(s):

    first_digit = s[0]
    second_digit = s[1]
    sum = int(first_digit) + int(second_digit)
    product = int(first_digit) * int(second_digit)
    return sum if sum > product else product

print(max_value('34'))

# or a better way
"""
a, b = map(int, s.split())
    return max(a + b, a * b)
    
"""
