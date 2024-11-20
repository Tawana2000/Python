# Write a function to check if a given number is aboth a square and a cubic number.
# To check if a number is both square and cubic, it must also be a perfect sixth power. This is because a number that is both a square (n = x^2) and a cube (n = x^3) satisfies n = z^6, where z is an integer

def sq_cu(n):

    if n < 0:
        return False
    
    i = 0

    while i ** 6 <= n:
        if i ** 6 == n:
            return True
        
        i += 1

    return False

print(sq_cu(64))