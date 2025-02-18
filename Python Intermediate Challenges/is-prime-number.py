# Write a function to check if a given number is prime or not

def is_prime(n):

    if n == 1 or n == 2:
        return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

print(is_prime(6))