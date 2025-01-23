# Write a function to find the nth star number

def nth_star_number(n):

    return 6 * n * (n - 1) + 1

print(nth_star_number(3))