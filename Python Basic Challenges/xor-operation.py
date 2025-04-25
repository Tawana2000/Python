# Write a function to perform the XOR operation on all elements of a list

def list_xor(numbers):

    result = 0
    for n in numbers:
        result ^= n

    return result

print(list_xor([1, 2, 3]))