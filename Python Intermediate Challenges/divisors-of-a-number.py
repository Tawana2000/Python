# Write a function to find all the divisors of a given number

def find_divisors(n):

    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors

n = int(input('Enter the number to find the divisors: '))
print(find_divisors(n))