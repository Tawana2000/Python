#write a function to find the minimum number of elements that need to be removed from a list of integers to make the sum of the remaining elements even

def min_removal(numbers):
     
    numbers.sort()
    sum1 = sum(numbers)
    if sum1 % 2 != 0:
        return 1
    else:
        return 0

    

numbers = input().split()
numbers = [int(n) for n in numbers]
print(min_removal(numbers))
