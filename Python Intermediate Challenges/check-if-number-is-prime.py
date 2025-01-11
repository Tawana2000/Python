# Write a function to check whether a number is prime or not

def is_prime(n):

    if n <= 1:
        return False  
    
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

n = int(input("Enter the number to check if it's prime: "))
print(is_prime(n))