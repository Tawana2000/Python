# Write a function to multiply all the digits of a number

def multiply_digits(n):

    n = abs(n)
    digits = str(n)

    result = 1

    for digits in digits:
        result *= int(digits)

    return result

n = int(input('Enter the number: '))
print(multiply_digits(n))