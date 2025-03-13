# Write a function to validate postal codes
# A valid postal code is a six digit number that does not contain more than on alternating repetitive digit pair 
# An alternating repetitive digit pair refers to two same digits separated by exactly one digit. For example, in 121426, 1 is an alternating repetitive digit because only one digit (2) comes in between the two 1s. However in 523563, there is no alternating repetitive digit because there are two digits (23) between the two 5s

def validate_postal_code(code):
 
    if not (isinstance(code, str) and len(code) == 6 and code.isdigit()):
        return False
    
    count = 0
    for i in range(4): 
        if code[i] == code[i + 2]:
            count += 1
    
    return count <= 1


print(validate_postal_code("121426")) 
print(validate_postal_code("523563"))
print(validate_postal_code("121212"))
print(validate_postal_code("123456"))
print(validate_postal_code("11"))