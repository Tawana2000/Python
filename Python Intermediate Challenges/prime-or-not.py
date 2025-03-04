# Write a function to check whether a number is prime or not. Return True if the number is prime. Else, return False

def is_prime(n):

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False
        
    return True

print(is_prime(7))
print(is_prime(6))