# Write a function to find the largest gap between consecutive numbers in a list

def largest_gap(numbers):

    if len(numbers) < 2:
        return 0
    
    numbers.sort()

    max_gap = 0

    for i in range(1, len(numbers)):
        gap = numbers[i] - numbers[i - 1]
        max_gap = max(max_gap, gap)

    return max_gap

numbers = [1, 6, 3, 8, 7]
print(largest_gap(numbers))