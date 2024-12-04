# Write a function to check if a given number is a pronic number or not

def is_pronic(n):

    for i in range(n):

        if n == i * (i + 1):
            return True
        

    return False

print(is_pronic(6))
print(is_pronic(5))