# Write a function to return the last letter of each number in a list

def end_letters(numbers):
    
    return [str(i)[-1] for i in numbers]

numbers = [123, 456, 789]
print(end_letters(numbers))