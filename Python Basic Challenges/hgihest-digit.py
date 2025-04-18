# Write a function to find the highest digit in a number

def highest_digit(n):

    sorted_n = ''.join(sorted(str(n)))
    max_number = sorted_n[-1]
    return int(max_number)

print(highest_digit(12354))