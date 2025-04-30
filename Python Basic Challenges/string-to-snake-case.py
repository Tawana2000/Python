# Write a function to convert a given string to snake case.

def to_snake_case(s):

    return s.lower().replace(" ", "_")

print(to_snake_case('Hello World'))