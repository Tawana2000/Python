# Write a function to rearrange the digits of the first number in a list to form the alrgest possible number

def maximize_first_number(numbers):

    numbers[0] = int(''.join(sorted(str(numbers[0]), reverse = True)))

    return numbers

numbers = [1234, 5678]
print(maximize_first_number(numbers))