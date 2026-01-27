# Write a function to flip the bits of a given integer

def flip_bits(n):

    num_bits = n.bit_length()
    
    mask = (1 << num_bits) - 1
    
    return n ^ mask

print(flip_bits(5))
print(flip_bits(0))
