# Write a functin to calculate the power of a number

def cal_power(base, exp):

    return base ** exp

base = int(input('Enter the base: '))
exp = int(input('Enter the exponent: '))

print(cal_power(base, exp))