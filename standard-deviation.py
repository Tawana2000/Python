# Write a function to find the standard deviation of a list of numbers

import statistics
def find_standard_deviation(numbers):

    result = statistics.stdev(numbers)
    new_result = round(result, 2)
    return new_result

numbers = list(map(int, input('Enter the list elements separated by space: ').split()))
print(find_standard_deviation(numbers))