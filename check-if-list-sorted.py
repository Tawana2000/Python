# Write a function to check if a given list of numbers is sorted in ascending order

def is_sorted(numbers):

    return True if sorted(numbers) == numbers else False

numbers = list(map(int, input('Enter the list elements separated by space: ').split()))

print(is_sorted(numbers))