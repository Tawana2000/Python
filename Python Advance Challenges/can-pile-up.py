# Write a function to determine if a given list of numbers can be piled up in a decreasing order
# The pile should start the with the largest number at the bottom and end with the smallest number at the top

def can_pile_up(numbers):
    while len(numbers) > 1:
        if numbers[0] >= numbers[-1]:
            numbers.pop(0)
        else:
            numbers.pop()
        if numbers and numbers[0] < numbers[-1]:
            return False
    return True

print(can_pile_up([4, 3, 2, 1]))  # True
print(can_pile_up([1, 3, 2, 4]))  # False
print(can_pile_up([5, 3, 4, 2, 1]))  # True
