#Create a list of first n natural numbers using list comprehension.

n = int(input('Enter the no of numbers to be printed: '))
list1 = [natural for natural in range(1,n+1)]
print(list1)