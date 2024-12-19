# Write a function to return 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, and 'FizzBuzz' for multiple of both 3 and 5

def fizz_buzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    
    elif n % 3 == 0 and n % 5 != 0:
        return 'Fizz'
    elif n % 3 != 0 and n % 5 == 0:
        return 'Buzz'
    
    else:
        return 'The number is not divisible by 3 or 5!'
    
n = int(input("Enter the number: "))
print(fizz_buzz(n))