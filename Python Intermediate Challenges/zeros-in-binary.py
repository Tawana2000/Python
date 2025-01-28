# Write a function to count the number of zeros in the binary representation of a given number

def count_zeroes(n):

    binary = bin(n)[2:]
    return binary.count('0')

print(count_zeroes(18))