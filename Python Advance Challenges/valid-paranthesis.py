# Write a function to determine if string contain just the valid parentheis

def is_valid(s):

    parenthesis = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = parenthesis.pop() if parenthesis else '#'
            if mapping[char] != top_element:
                return False
        else:
            parenthesis.append(char)

    return not parenthesis

print(is_valid('[]'))
print(is_valid('""'))
print(is_valid("([)]")) 
print(is_valid("(([]))")) 