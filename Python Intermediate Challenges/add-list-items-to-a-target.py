# Write a function to check if there are two numbers in a list that add up to a target value

def check_sum(numbers, target):

    items = set()
    for i in numbers:
        if target - i in items:
            return True
        items.add(i)

    return False

numbers = [1, 2, 3, 4]
target = 5
print(check_sum(numbers, target))