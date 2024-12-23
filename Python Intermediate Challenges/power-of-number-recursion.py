#Program to find power of a number using recursion

def find_power(base, power):

    if power == 0:
        return 1
    
    else:

        return find_power(base, power - 1) * base
    
base = int(input())
power = int(input())

print(find_power(base, power))