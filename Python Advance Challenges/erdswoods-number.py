# Write a function to determine if a number is an Erdswoods number
# An Erdswoods number is a positive integer that cannot be written as the sum of the squares of two integers

def is_erdswoods(n):

    if n < 0:
         return 'Choose a positive number!'
    
    i = 0
    while i * i <= n:
        j = 0
        while j * j <= n - i * i:
            if i * i + j * j == n:
                return False
            j += 1
        i += 1

    return True

print(is_erdswoods(3))
print(is_erdswoods(13))