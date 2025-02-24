# Write a function to find the odd integers from a given list of numbers

def odd_numbers(numbers):

    result = []

    for i in numbers:
        if i % 2 != 0:
            result.append(i)

    return result

numbers = [1, 2, 3, 4, 5, 6]
print(odd_numbers(numbers))