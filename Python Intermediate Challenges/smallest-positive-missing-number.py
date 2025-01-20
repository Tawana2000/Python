# Write a function to find the smallest missing positive integer from a list

def find_missing(numbers):

    l = len(numbers)

    for i in range(l):
        while 1 <= numbers[i] <= l and numbers[numbers[i] - 1] != numbers[i]:
            numbers[numbers[i] - 1], numbers[i] = numbers[i], numbers[numbers[i] - 1]

    for i in range(l):
        if numbers[i] != i + 1:
            return i + 1
        

    return l + 1

numbers = [3, 4, -1, 1]
print(find_missing(numbers))