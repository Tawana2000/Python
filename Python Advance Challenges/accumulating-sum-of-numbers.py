# Write a funtion to calculate the accumulating sum of list of numbers

def running_sum(numbers):
    result = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        result.append(current_sum)
    return result

print(running_sum([1, 2, 3, 4]))
