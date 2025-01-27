# Write a function to check if difference between all consecutive pairs are 2

def two_difference(numbers):

    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) != 2:
            return False
        
    return True

print(two_difference([1,3,5,7,9]))