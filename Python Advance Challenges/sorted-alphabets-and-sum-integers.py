#Create a Python program to rearrange a string by sorting the alphabetic characters, followed by the sum of all digits, for ex: for the string '9python123' out put should be: hnopty15

def sort_alph(string):

    number = []
    new_str = ''

    for char in string:

        if char .isdigit():
            number.append(int(char))

        else:
            new_str += char
    
    
    new_str = sorted(new_str)    #it gives us a list then we can use join() to sort the string
    new_str = ''.join(new_str)

    sum_numbers = sum(number)

    result = new_str + str(sum_numbers)
    print(result)

sort_alph('9python123')
