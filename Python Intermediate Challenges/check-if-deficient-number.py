# Write a function to check if a number is deficient
# A number is deficient if the sum of its proper divisors is less than the number itself

def is_deficient(n):

    result = []

    for i in range(1, n):
        if n % i == 0:
            result.append(i)

    if sum(result) < n:
        return True
    
    else:
        return False
    
n = int(input("Enter a number to check if deficient: "))
print(is_deficient(n))