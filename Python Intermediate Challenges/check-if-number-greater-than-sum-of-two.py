# Write a function to check if a number is greater than the sum of the two numbers 

def greater_than_sum(number):

    number.sort()

    return True if number[2] > (number[0] + number[1]) else False

number = [1, 2, 4]
print(greater_than_sum(number))