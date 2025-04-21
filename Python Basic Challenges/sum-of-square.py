# Write a function to calculate the sum of all square numbers in a list

def sum_of_squares(numbers):
    
    squares = []

    for nums in numbers:

        squares.append(nums ** 2)
    return sum(squares)    
    
print(sum_of_squares([2, 3, 4]))
