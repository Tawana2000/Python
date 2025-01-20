# Write a function to check if a number is a repdigit or not
# Ripdigit is a positive number composed out of the same digit

def is_repdigit(number):

    str_number = str(number)

    return len(set(str_number)) == 1

print(is_repdigit(111111))
print(is_repdigit(12352))