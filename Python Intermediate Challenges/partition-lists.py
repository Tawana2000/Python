# Write a function to partition a list of integers into two lists: one containing all even numbers and the other containing all odd numbers

def even_odd_partition(numbers):

    odd = []
    even = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        
        else:
            odd.append(i)

    return even, odd

numbers = [1, 2, 3, 4, 5]
print(even_odd_partition(numbers))