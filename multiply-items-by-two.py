#Write a python function to multiply every item in a list by two

def multi(numbers):
    

    result = []

    for i in numbers:
        i = i * 2
        result.append(i)

    return result

numbers = [1,2,3,4]
print(multi(numbers))