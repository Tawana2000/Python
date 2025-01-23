# Write a function to check if a number is an Achilles number or not

def is_powerful(n):
    if n < 1: return False
    for i in range(2, n + 1):
        if n % i == 0:
            if n % (i * i) != 0: return False
            while n % i == 0: n //= i
    return True

def is_perfect_power(n):
    for base in range(2, int(n**0.5) + 1):
        power = base * base
        while power <= n:
            if power == n: return True
            power *= base
    return False

def is_achilles(n):
    return is_powerful(n) and not is_perfect_power(n)

# Example usage
number = int(input("Enter a number: "))
if is_achilles(number):
    print(f"{number} is an Achilles number.")
else:
    print(f"{number} is not an Achilles number.")