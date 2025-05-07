# Write a function to implement Euler's Totient Function 
# Two numbers are said to be relatively prime if their greatest common divisor (gcd) is 1.
# Euler's Totient Function, is used to determine the number of positive integers less than n, which are relatively prime to n

def eulers_totient(n):
    
    count = 0

    for i in range(1, n + 1):

        a, b = n, i
        while b:
            a, b = b, a % b

        if a == 1:
            count += 1

    return count

print(eulers_totient(9))
print(eulers_totient(20))
print(eulers_totient(33))
