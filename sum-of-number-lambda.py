#Sum of two numbers using lambda function
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
sum = lambda a,b: a + b
print("Sum of the entered numbers is=", sum(a,b))
