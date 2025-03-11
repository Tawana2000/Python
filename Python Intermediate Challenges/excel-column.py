# Write a function to convert a given integer to an Excel sheet column title 
# In Excel, columns are name with letters. The first 26 columns are labeled with the letters A to Z and then start again with AA, AB and so on.

def convert_to_title(n):

    result = ""

    while n > 0:
        n -= 1
        result = chr(n % 26 + ord('A')) + result
        n //= 26

    return result

print(convert_to_title(28))
print(convert_to_title(4))
print(convert_to_title(789))