# Write a function to check whether the given number is a factorial prime
# A factorial prime is a prime number that is one less or one more than a factorial (all factorials greater than 1 are even)

def is_facotrial(num):
    
    if num < 2 or num % 2 == 0 and num != 2:
        return False
    
    factorial = 1

    for i in range(1, num):
        factorial *= i
        if num == factorial - 1 or num == factorial + 1:
            return True
        
    return False

print(is_facotrial(5))
print(is_facotrial(8))