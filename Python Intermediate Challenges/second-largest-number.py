# Write a function to find the second largest number in a list

def second_largest(lst):
    unique_numbers = list(set(lst))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None


print(second_largest([1, 2, 3, 4, 5])) 
print(second_largest([5, 5, 5])) 
