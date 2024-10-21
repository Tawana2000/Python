# We can use if ... else statement to stop the recursion which is also called base case
""""
def calculate(number):

    if number == 20:
        return
    print(number)

    calculate(number + 1)

calculate(10)
"""

#or

"""
def calculate(number):

    if number == 20:
        return "Done"
    
    print(number)

    return calculate(number + 1)
print(calculate(10))
"""


#or

def calaculate(number):

    if number == 6:
        return "Done"
    
    print(number)

    return calaculate(number + 1) + "over"


print(calaculate(3))