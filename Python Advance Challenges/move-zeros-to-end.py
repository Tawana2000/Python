# Write a function to move all the zeros in an integer to the end.

def move_zeros_to_end(n):

    s = str(n)

    non_zeros = [digit for digit in s if digit != '0']
    zeros = s.count('0')

    result = ''.join(non_zeros) + '0' * zeros
    return int(result)

print(move_zeros_to_end(1020304050))
