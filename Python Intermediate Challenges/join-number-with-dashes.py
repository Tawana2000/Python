# Write a function to join the digits of a number with dashes

def join_digits_with_dashes(n):

    return "-".join(str(n))

print(join_digits_with_dashes(123456))