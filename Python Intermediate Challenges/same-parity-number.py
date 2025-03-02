# Write a function to check if a number has the same parity as the sum of its digits

def check_parity(number):

    sum_digit = sum(int(digit) for digit in str(number))

    return (number % 2 == sum_digit % 2)
    
print(check_parity(123))