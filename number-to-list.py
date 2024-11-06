# Write a function to convert a number into a list of its digits in reverse order

def num_to_list(number):
    number = [int(digit) for digit in str(number)]
    number.reverse()
    return number

number = 34342
print(num_to_list(number))