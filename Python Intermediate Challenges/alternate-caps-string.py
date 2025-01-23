# Write a function to convert a given string into alternating caps

def alternating_caps(s):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))

input_string = "hello world"
result = alternating_caps(input_string)
print(result)