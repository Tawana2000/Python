# Write a function to implement the Collatz Conjecture

def collatz_conjecture(n):

    result = [n]

    while n != 1:
        if n % 2 == 0:
            n //= 2
        
        else:
            n = 3 * n + 1

        result.append(n)

    return result

print(collatz_conjecture(6))