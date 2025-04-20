# Write a function to determine if a number is a circular prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_rotations(num):
    str_num = str(num)
    rotations = []
    for i in range(len(str_num)):
        rotated = str_num[i:] + str_num[:i]
        rotations.append(int(rotated))
    return rotations

def is_circular_prime(num):
    if not is_prime(num):
        return False
    rotations = get_rotations(num)
    return all(is_prime(rot) for rot in rotations)

# Example Usage
number = 197
if is_circular_prime(number):
    print(f"{number} is a circular prime.")
else:
    print(f"{number} is not a circular prime.")
