#Write a function to find the largest number in list

def largest(number):

    number.sort()
    return number[-1]

number = [1, 2, 3, 4, 5]
print(largest(number))