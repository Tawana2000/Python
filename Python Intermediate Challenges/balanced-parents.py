# Write a function that checks if the parentheses in a string are balanced

def is_balanced(s):
    stack = []
    parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if not stack or stack.pop() != parentheses[char]:
                return False
    return not stack

print(is_balanced("((()))")) 
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}")) 
