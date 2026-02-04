# Write a function to swap 0s and 1s from the binary representation of a number

def binary_toggle(n):

    if n < 0:
        return n
    return n ^ ((1 << (n.bit_length() or 1)) - 1)

print(binary_toggle(5))
