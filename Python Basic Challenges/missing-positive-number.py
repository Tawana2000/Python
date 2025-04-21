# Write a function to find the first missing positive number in a given list of numbers

def find_missing_number(numbers):
    
    numbers = set(numbers)
    i = 1
    while i in numbers:
        i += 1

    return i
            
print(find_missing_number([1, 3, 4]))
