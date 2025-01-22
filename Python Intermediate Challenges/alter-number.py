# Write a function to alter a list of numbers such that even numbers are halved and 1 is subtracted from odd numbers

def alter_numbers(numbers):

    result = []

    for i in numbers:
        if i % 2 == 0:
            result.append(i/2)
        
        else:
            result.append(i - 1)

    return result

numbers = [2, 3, 4, 5]
print(alter_numbers(numbers))