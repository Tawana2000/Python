# Write a function to check if a number is prime within a given range

def is_prime_in_range(n, start, end):

    for i in range(start, end + 1):
        if n % i == 0 and i != 1 and i != n:
            return False
        
    return True

n = int(input('Enter the number to check: '))
start = int(input('Enter the starting boundary: '))
end = int(input('Enter the ending boundary: '))

print(is_prime_in_range(n, start, end))