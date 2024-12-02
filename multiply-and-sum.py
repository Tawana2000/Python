# Write a function to multiply two numbers and return the sum of the result and the first number

def sum_of_multiplication(num1, num2):

    return (num1 * num2) + num1

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print(sum_of_multiplication(num1, num2))