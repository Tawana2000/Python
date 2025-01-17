# Write a function to negate a given regular expression

def negate(string):

    neg = "[" + "^" + string + "]"
    return neg

string = 'abc'
print(negate(string))