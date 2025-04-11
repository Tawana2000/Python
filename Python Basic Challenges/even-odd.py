# Write a function to elemenate all the odd numbers from a list

def eliminate_odd_numbers(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)

    return result
print(eliminate_odd_numbers([1, 2, 3, 4, 5, 6])
