# Write a function fo calculate the Euler number to a specified precision

def calculate_euler(precision):

    fact = 1
    euler_value = 1

    for i in range(1, 100):
        fact *= i
        euler_value += 1 / fact

    return euler_value

print(calculate_euler(5))
    
