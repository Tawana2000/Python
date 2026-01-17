# Python program to add commas to a number to separate the thousands

def thousands_sep(number):

    number = str(number) [::-1]    #convert the number to string and reverse
    separated = ''   #empty string to store the result

    for i in range(0, len(number)):

        if i % 3 == 0 and i != 0:
            separated += ','  #add comma to separated string

        separated += number[i] #add number to the separated string

    return separated[::-1] # reverse again to convert back to its original

result = thousands_sep(10000000)
print(result)
