# Write a function to check if all numbers in a given list are prime.

def all_primes(numbers):

    for num in numbers:

        if num < 2 or any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)):
            return False
        
    return True


print(all_primes([2, 3, 5]))
print(all_primes([4, 8, 7, 13]))
print(all_primes([6, 9, 2, 1, 13]))
