# Write a function to add two binary strings and return their sum as a binary 

def add_binary(a, b):

    decimal_result = int(a, 2) + int(b, 2)
    return bin(decimal_result)[2:]

print(add_binary("11", '1'))