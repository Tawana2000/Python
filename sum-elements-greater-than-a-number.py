# Write a function to calculate the sum of elements in a list that are greater than a given number

def sum_greater(numbers, n):

    new_list = []

    for items in numbers:

        if items > n:
            new_list.append(items)

            result = sum(new_list)

    return result

numbers = map(int, input('Enter the list of numbers separated by space: ').split())
n = int(input('Enter the number to check: '))

print(sum_greater(numbers, n))