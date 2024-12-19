# Write a function to split a string at each capital letter

def capital_split(s):

    result = []
    current_substr = ""

    for char in s:
        if char.isupper():
            if current_substr:
                result.append(current_substr)
            current_substr = char

        elif char.islower():
            return '[]'
            
        else:
            current_substr += char

    if current_substr:
        result.append(current_substr)
    
    return result

s = input('Enter the string: ')
print(capital_split(s))