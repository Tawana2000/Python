# Write a function to calculate the number of derangements for a given number

def count_derangements(n):

    if n <= 0: return 1 if n == 0 else 0
    if n == 1: return 0
    a, b = 1, 0
    
    for i in range(2, n + 1):
        a, b = b, (i - 1) * (a + b)

    return b

print(count_derangements(4))