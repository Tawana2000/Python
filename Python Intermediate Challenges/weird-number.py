# Write a function to check if a number is weird

def is_weird(n):

    if n % 2 != 0:
        return 'Weird'
    
    if n >= 2 and n <= 5:
        return 'Weird'
    
    if n % 2 == 0 and n >= 6 or n <= 20:
        return 'not weird'
    
    else:
        return 'not weird'
    
print(is_weird(3))