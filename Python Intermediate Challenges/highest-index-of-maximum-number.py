# Write a function to find the highest index of the maximum number in a list

def get_max_and_last_index(numbers):
    
    if not numbers:
        return None, None
    max_value = max(numbers)
    max_index = len(numbers) - 1 - numbers[::-1].index(max_value)
    return max_value, max_index

numbers = [1, 2, 3, 2, 1, 3]
print(get_max_and_last_index(numbers))
