# Write a function that takes a floating point as input and returns the reverse of that number

def reverse_number(n):

    str_n = str(n)
    reversed_n = str_n[::-1]
    return float(reversed_n)

print(reverse_number(123.45))