# Write a function to calculate the accumulating product of a list of numbers

def accumulating_product(numbers):
    
    if not numbers:
        return []
    
    product_list = []
    product = 1

    for i in numbers:

        product *= i
        product_list.append(product)

    return product_list
    
numbers = [1, 2, 3, 4]
print(accumulating_product(numbers))