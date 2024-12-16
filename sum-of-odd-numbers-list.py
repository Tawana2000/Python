# Write a function to find the sum of odd numbers in a list

def sum_of_odd(numbers):

    odd_numbers = []

    for i in numbers:
        if i % 2 != 0:
            odd_numbers.append(i)

    return sum(odd_numbers)
    
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
print(sum_of_odd(numbers))