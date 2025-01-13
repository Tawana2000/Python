# Write a function to calculate the lowest common multiple (LCM) of two numbers

def calculate_lcm(num1, num2):

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    return abs(num1 * num2) // gcd(num1, num2)

num1 = 12
num2 = 15
print(calculate_lcm(num1, num2))