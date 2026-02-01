#write a python function to find the sum of the two smallest number in a list

def sum_of_smallest(numbers):

    numbers.sort()

    result = numbers[0] + numbers[1]
    return result

numbers = input().split()
numbers = [int(n) for n in numbers]
print(sum_of_smallest(numbers))
