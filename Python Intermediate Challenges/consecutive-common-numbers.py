# Write a function to check if a list contains three consecutive common numbers

def check_consecutive_numbers(numbers):

    for i in range(len(numbers) - 2):

        if numbers[i] == numbers[i + 1] == numbers[i + 2]:
            return True
        
    return False
    
print(check_consecutive_numbers([1, 2, 2, 2, 5]))
print(check_consecutive_numbers([5, 6, 2, 13, 4, 4]))
