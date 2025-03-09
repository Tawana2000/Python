# Write a function to calculate the nth pentagonal number
# A pentagonal number is a figurate number that extends the concept of triangular and square numbers to the pentagon. The nth pentagonal number P is given by the formula p = n * (3 * n - 1)/2

def pentagonal_number(n):

    return n * (3 * n - 1) / 2

print(pentagonal_number(5))