# Write a function to remove all the prime numbers from a given list

def remove_primes(numbers):

    result = []

    for num in numbers:
        if num < 2:
            result.append(num)
            continue

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                result.append(num)
                break

    return result

numbers = [2, 3, 4, 5]
print(remove_primes(numbers))