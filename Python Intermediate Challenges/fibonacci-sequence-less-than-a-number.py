# Write a function to get the Fibonacci sequence less than a given number

def fibonacci_less_than(n):
    
    result = [0, 1]
    while result[-1] + result[-2] < n:
        result.append(result[-1] + result[-2])
    return result

print(fibonacci_less_than(50))