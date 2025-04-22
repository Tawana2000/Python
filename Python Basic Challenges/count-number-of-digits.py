# Write a function to count the number of digits in a given number.

def count_digits(n):

    count = 0

    for i in range(1, len(str(n)) + 1):
        count += 1

    return count

print(count_digits(12345))