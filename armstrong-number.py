#Write a program to find if the given number is an Armstrong Number.
#An Armstrong number (for a 3-digit number) is a number where the sum of the cube of each digit is equal to the original number, ex: 371

def armstrong(number):

    sum = 0

    for digits in number:

        num = int(digits)

        sum += num ** 3

    if sum == int(number):
        return 'Armstrong Number'
    
    else:
        return 'Not Armstrong Number'
    
number = input()
print(armstrong(number))