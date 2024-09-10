#Given any number, find the factors of that number. Then, return the sum of odd factors.

def sum_odd(number):

    factors = []

    for i in range(1,number + 1):
        if number % i == 0:
            factors.append(i)

    sum = 0

    for j in factors:
        if j % 2 != 0:
            sum += j
    print(sum)
    return False

number = 18
sum_odd(number)
        
        
    
    
