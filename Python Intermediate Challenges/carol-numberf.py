# Write a function to generate the nth Carol number
# Carol numbers are a sequence of integers (starting from 0) that follow this formula: (2^n - 1)^2 - 2

def carol_number(n):

    return (2**n - 1)**2 - 2

n = int(input("Enter the nth number to find the Carol value: "))
print(carol_number(n))