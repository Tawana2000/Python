# Write a function to check if a given number is a pronic number or not
# A pronic number (or otherwise known as Heteromecic number), is a product of two consecutive integers

def is_pronic(n):

    for i in range(n):

        if n == i * (i + 1):
            return True
    return False
    
print(is_pronic(42))
print(is_pronic(21))