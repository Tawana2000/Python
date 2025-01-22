# Write a function to perform numerical morphisms

def transform_digits(n):
    n_str = str(n)
    result = ''.join(str(int(d) + 1) if d != '9' else '10' for d in n_str)
    return result


print(transform_digits(1234)) 
print(transform_digits(9999))