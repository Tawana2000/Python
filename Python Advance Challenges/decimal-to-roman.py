# Write a function to convert a decimal number lying between 1 and 3999 to Roman numerals

def decimal_to_roman(num):

    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    
    result = ""

    for i in roman:
        result += roman[i] * (num // i)
        num %= i

    return result

print(decimal_to_roman(1880))
print(decimal_to_roman(1423))
print(decimal_to_roman(985))
