# Write a function to help jump across an array
# The frog can only jump forward and it jumps frome one number to the next higher number, don't jump unless there's a higher number going forward

def frog_jump(numbers):
    
    if not numbers:
        return 0
    
    jump_count = 0
    current = numbers[0]

    for i in numbers[1:]:
        if i > current:
            jump_count += 1
            current = i

    return jump_count

    
numbers = [2, 1, 3, 4]
print(frog_jump(numbers))