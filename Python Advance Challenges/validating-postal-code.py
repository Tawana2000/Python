# Write a function to validate a postal code
# A valid postal code must follow the pattern DDD-DDD, where D is a digit

import re
def validate_postal_code(code):

    return bool(re.match(r'^\d{3}-\d{3}$', code))

def validate_postal_code_no_regex(code):
    if len(code) != 7:
        return False
    
    if code[3] != '-':
         return False
    
    digits = code[:3] + code[4:]
    return digits.isdigit()

print(validate_postal_code("123-456"))
print(validate_postal_code("123-45"))
