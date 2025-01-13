# Write a function to check if a given number is and ugly number
# An ugly number is a positive integer whose prime factors only include 2, 3 and 5

def is_ugly(num):

    if num <= 0:
        return False
    
    for i in [2, 3, 5]:
        while num % i == 0:
            num //= i

    return num == 1

print(is_ugly(6))
print(is_ugly(14))