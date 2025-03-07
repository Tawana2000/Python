# Write a function to check if a number is pandigital

def is_pandigital(n):

    return set(str(n)) == set("0123456789")

print(is_pandigital(1234567890))