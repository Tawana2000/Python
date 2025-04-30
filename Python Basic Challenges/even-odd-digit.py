# Write a function to check if a two-digit number has one even and one odd digit.

def check_number(number):
    tens = number // 10
    units = number % 10 
    return (tens % 2 == 0 and units % 2 != 0) or (tens % 2 != 0 and units % 2 == 0)

print(check_number(23))
print(check_number(33))