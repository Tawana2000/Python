# Write a function to find the nearest element to a given number in a list 

def nearest_element(numbers, target):

    if not numbers:
        raise ValueError("The list is empty!")
    
    nearest = min(numbers, key=lambda n: abs(n - target))
    return nearest

numbers = [7, 11, 23]
target = 10

result = nearest_element(numbers, target)
print(F"The nearest number to {target} is {result}.")