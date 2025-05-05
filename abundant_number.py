#Write a program to find if the passed number is an Abundant Number.
#An abundant number is any number whose proper factors' sum is greater than the number itself. for ex: 18 ---> 1,2,3,6,9


def abd_num(number):

    factors = []

    for i in range (1, number):

        if number % i == 0:
            factors.append(i)
            
    if sum(factors) > number:
        return 'It is an Abundant Number'
            
    else:
        return 'It is not an Abundant Number'
            
number = int(input())
print(abd_num(number))
            
