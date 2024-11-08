# Write a function to create a fucntion that adds two numbers and appends the result
# For inputs 2 and 3, the output should be 235 (2 + 3 = 5 and adding all 3 it will be 235)

def add_numbers(num1, num2):
    
    result = num1 + num2
    if num1 == 0 and num2 == 0 and result == 0:
        return 0

    else:
        result2 = str(num1) + str(num2) + str(result)
        return result2
    
num1 = int(input())
num2 = int(input())
print(add_numbers(num1, num2))