# Write a function to get Fibonacci sequence

def fibonacci(n):
    
    if n == 0 or n == 1:
        return [0]
    
    result = [0, 1]

    for i in range(2, n):
        result.append(result[-1] + result[-2])
    return result

print(fibonacci(7))
        