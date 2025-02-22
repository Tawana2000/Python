# Write a funtion to find the product of the two largest numbers in a list

def product_of_largest(numbers):

    numbers.sort()
    return numbers[-1] * numbers[-2]

numbers = [4, 1, 3, 5, 6]

print(product_of_largest(numbers))