# Write a function to swap two given integers

def swap_numbers(num1, num2):

    num1, num2 = num2, num1

    return num1, num2

print(swap_numbers(3, 4))