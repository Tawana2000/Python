# Write a function to filter out and return only the positive numbers from a list

def positive_filter(numbers):

    positive_numbers = []

    for i in numbers:
        if i > 0:
            positive_numbers.append(i)

    return positive_numbers


numbers = [-1, 2, -3, 4, -5]
print(positive_filter(numbers))