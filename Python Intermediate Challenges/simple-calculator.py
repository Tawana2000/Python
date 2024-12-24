# Make a simple calculator in python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# choising the operations
print("Operation: +, -, *, /")
select = input("Select operations: ")

# addition
if select == "+":
    print(num1, "+", num2, "=", num1+num2)

# subtraction
elif select == "-":
    print(num1, "-", num2, "=", num1-num2)

# multiplication
elif select == "*":
    print(num1, "*", num2, "=", num1*num2)

# division
elif select == "/":
    print(num1, "/", num2, "=", num1/num2)

else:
    print("Please enter a valid input")
