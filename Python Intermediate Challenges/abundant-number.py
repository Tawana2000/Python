# Write a function to check if a number is abundant or not

def is_abundant(n):

    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    sum_divisors = sum(divisors)

    if n > sum_divisors:
        return False
        
    return True

n = int(input("Enter the number to check if abundant: "))
print(is_abundant(n))