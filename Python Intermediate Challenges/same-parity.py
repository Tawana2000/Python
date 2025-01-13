# Write a function to return a list that contains elements with the smae parity (odd or even) as the first element of the list

def same_parity(numbers):

    even = []
    odd = []
    result = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    if numbers[0] % 2 == 0:
        return even
    else:
        return odd
        
numbers = [1, 2, 3, 4]
print(same_parity(numbers))