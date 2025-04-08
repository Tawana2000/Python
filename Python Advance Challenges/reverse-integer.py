# Write a function to reverse an integer without converting it to string

def reverse_integer(n):

    sign = 1 if n>= 0 else -1 
    n = abs(n)

    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    if reversed_num > 2 ** 31 - 1 or reversed_num < -2 ** 31:
        return 0
    
    return sign * reversed_num

print(reverse_integer(12345))