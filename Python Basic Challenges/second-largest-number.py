# Write a function to find the second largest number from a given list.
"""
def second_largest(number):

    number.remove(max(number))
    return max(number)

print(second_largest([1, 2, 3, 4, 5]))
"""
# OR

def second_largest(number):
    
    number.sort()
    number = list(set(number)) # Remove duplicates
    return number[-2]
print(second_largest([3, 4, 2, 1, 5, 5]))