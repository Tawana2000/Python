# Write a function to check if a number is a Harshad number or not
# A Harshad number in a given number base is an integer that is divisible by the sum of its digits when written in that base

def is_harshad(n):
    
    result = 0
    for num in str(n):
    

        result += int((num))

    if n % result == 0:
        return True
    
    else:
        return False
    
print(is_harshad(18))
print(is_harshad(28))
print(is_harshad(33))
