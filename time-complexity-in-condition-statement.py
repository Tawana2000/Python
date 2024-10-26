#In a conditional statement, such as if..else, a certain block of code may be skipped from execution.
#Suppose we have a program like this.

def print_numbers(n):

    if n > 100:                         # 1 unit of time
        print(n)                        # 1 unit of time

    else:
        for i in range(n):              # n units of time    
            print(n)                    # n units of time
 
num = int(input("Enter a number: "))
print_numbers(num)


"""
1. if n is greater than 100
the if block is executed and the value of n is printed once


2. if n is less than or equal to 100
the loop inside th eelse block is executed 

Hence
if n > 100, the TC = O(1)

if n is less than or equal to 100, the TC = O(n)

"""