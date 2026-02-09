# Write a function to calculate the home prime of a number

def home_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    while not is_prime(n):
        factors, divisor = [], 2
        temp = n
        while temp > 1:
            while temp % divisor == 0:
                factors.append(str(divisor))
                temp //= divisor
            divisor += 1
        n = int("".join(factors))

    return n

print(home_prime(4)) 
print(home_prime(10)) 
print(home_prime(12))  
