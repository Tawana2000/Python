#Write a function to map each lowercase letter in a string to its corresponding uppercase letter and vice versa 

def case_swap(s):

    result = s.swapcase()
    return result

s = 'Hello World'
print(case_swap(s))