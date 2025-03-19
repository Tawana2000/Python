# Write a function to extract all the numbers from a given string

def extract_numbers(s):

    result = ''

    for chars in s:
        if chars.isdigit():
            result += chars

    return result if result else None

print(extract_numbers('hello123world456'))
print(extract_numbers('NoNumbersHere'))