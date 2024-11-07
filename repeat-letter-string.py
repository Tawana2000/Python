# Write a function to repeat each letter in a string n times
#for input 'abc', 3.  The output should be: 'aaabbbccc'

def repeat_ltr(s, n):

    result = ""

    for i in s:
        result += i * n
    return result
s = 'abc'
n = 3
print(repeat_ltr(s, n))