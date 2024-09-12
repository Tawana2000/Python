#Write a Python program that returns a string representation of numbers 1 to n.
#But instead of numbers that are divisible by 3, it should print 'Fizz' and instead of numbers that are divisible by 5, it should output 'Buzz'

def fizzbuzz(n):

    numbers = []

    for i in range(1, n + 1):

        if i % 3 == 0:
            numbers.append('Fizz')

        elif i % 5 == 0:
            numbers.append('Buzz')

        else:
            numbers.append(str(i))

    return numbers


n = int(input())

print(fizzbuzz(n))