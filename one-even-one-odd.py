# Write a function to check if a two digit number has one even and one odd digit

def even_odd(number):
    tens = number // 10
    units = number % 10
    return (tens % 2 == 0 and units % 2 != 0) or (tens % 2 != 0 and units % 2 == 0)

# Testing the function
print(even_odd(22)) 
print(even_odd(23)) 
print(even_odd(57))