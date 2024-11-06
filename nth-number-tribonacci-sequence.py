# Write a function to generate the nth number in the Tribonacci sequence

def tri_seq(n):
    
    if n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c

n = 6

print(f"The {n}th number in the Tribonacci series is: {tri_seq(n)}")