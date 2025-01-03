# Write a function to calculate the power of a number

def power_number(base, power):

    return base ** power

base = int(input("Enter the number: "))
power = int(input("Enter the desired power: "))
print(power_number(base, power))
