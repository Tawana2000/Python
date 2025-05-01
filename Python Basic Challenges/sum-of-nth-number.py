# Write a function to calculate the sum of every nth number in a list

def sum_nth_numbers(numbers, n):

    return sum(numbers[i] for i in range(n - 1, len(numbers), n))

print(sum_nth_numbers([1, 2, 3, 4, 5, 6], 2))