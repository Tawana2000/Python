# Write a function to calculate the product of all items in a list

def product_items(numbers):
    
    result = 1

    for i in numbers:
        result *= i

    return result

numbers = [2, 3, 4]
print(product_items(numbers))