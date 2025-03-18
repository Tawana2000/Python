# Write a function to check if a number is Disarium or not
# A number is considered Disarium when the sum of its didits, each raised to the power of their respective positions, equals the number itself

def is_disarium_number(num):

    total = 0
    pos = 1

    for digit in str(num):
        total += int(digit) ** pos
        pos += 1

    return total == num

print(is_disarium_number(75))
print(is_disarium_number(89))