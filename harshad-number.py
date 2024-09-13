#Write a Python program to find if the given number is a Harshad Number.
#Harshad Number is any number where the number itself is divisible by the sum of the digits in the number.

def harshad(number):

    sum = 0

    for digits in number:

        sum += int(digits)

    if int(number) % sum == 0:
        return 'It is a Harshad Number'
        
    else:
        return 'It is not a Harshad Number'
        
number = input()
print(harshad(number))