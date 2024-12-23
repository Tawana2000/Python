#Program to find the number in the nth position of Fibonaccin series
# 0,1,1,2,3,5,8,.......       nth number position = (n - 1)th + (n - 2)th 

def fib(number):

    if number == 0 or number == 1:
        return number
    
    return fib(number - 1) + fib(number - 2)

number = 6
print(fib(number))
