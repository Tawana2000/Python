#program to print only odd numbers of a list

number = [2,23,12,67,13,29,34,48,9]

for i in number:
    if i % 2 != 0:
        print(i)

# or to print the odd numbers using list comprehension
only_odd = [num for num in number if num % 2 == 1]
print(only_odd)