# Write a function to reverse a given number.

def reverse_number(n):

    str_n = str(n)
    return str_n[::-1]

print(reverse_number(12345))