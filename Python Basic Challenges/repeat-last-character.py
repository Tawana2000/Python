# Write a function to repeat the last character of a string n times

def repeat_last_character(string, n):

     return string[:-1] +  string[-1] * n

print(repeat_last_character('hello', 3))
print(repeat_last_character('python', 6))
