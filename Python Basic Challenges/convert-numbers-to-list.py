# Write a function to convert a number into a list of its digits and vice versa

def to_from_list(n):

    if isinstance(n, int):
        return [int(digit) for digit in str(abs(n))]
    
    return int(''.join(map(str, n)))

print(to_from_list(1234))
print(to_from_list([4, 5, 3, 2, 1]))