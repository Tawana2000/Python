# Write a function to check if a given number is Pandigital

def is_number_pandigital(num):
    
    return sorted(str(num)) == list("0123456789")

num = 1234567890
print(is_number_pandigital(num))