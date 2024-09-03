#You are given two numbers but in string format. Now, you need to multiply them and return the multiplication, that too in a string format.
#For example, if the given strings are '12' and '10', your program should return '120'.

def multiply(str1,str2):

    num1 = int(str1)
    num2 = int(str2)

    num3 = num1 * num2

    result = str(num3)

    print(result)

multiply('10','12')