# Write a function to calculate the nth Bernoulli number

def bernoulli_number(n):
    A = [1 / (i + 1) for i in range(n + 1)] 
    
    for m in range(1, n + 1):
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j]) 

    return round(A[0], 4)

print(bernoulli_number(8))
