# Write a function to convert an Excel sheet column title to its corresponding column number

def excel_column_number(column_title):

    result = 0

    for char in column_title:
        result = result * 26 + (ord(char) - ord('A') + 1)

    return result

print(excel_column_number('AB'))
print(excel_column_number('GI'))
