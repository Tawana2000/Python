# Write a function to generate the nth Euclid number
# A Euclid number is a positive integer of the form p# + 1, where p# is the product of the first p prime numbers

def euclid_number(n):

    p, num = 1, 2

    while n:
        if all(num % i for i in range(2, int(num ** 0.5) + 1)):
            p *= num
            n -= 1

        num += 1

    return p + 1

print(euclid_number(5))