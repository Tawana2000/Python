# Write a function to check if a given number is composite or not
# A composite number is any positive integer greater than one that is not a prime number

def is_composite(n):

    if n <= 1:
        raise ValueError("Please enter a positive number greater than one!")
    
    for i in range(2, n + 1):
        return True if n % i == 0 else False
  
        
n = int(input("Enter a number to check if composite or not: "))
print(is_composite(n))