# Write a function to calculate the primorial of a number

def calculate_primorial(n):
    def is_prime(x):
        return x > 1 and all(x % i for i in range(2, x))

    p = 1
    for num in range(2, n + 1):
        if is_prime(num):
            p *= num

    return p

n = int(input("Enter the number: "))
print(calculate_primorial(n))
