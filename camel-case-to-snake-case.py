#Now, write a Python program that converts camelCase strings to snake_case.

def cam_snake(string):

    snake_case = ''

    for index, char in enumerate(string):

        if char.isupper():

            if index != 0:
                snake_case += '_'

            snake_case += char.lower()

        else:
            snake_case += char

    return snake_case

string = input()
print(cam_snake(string))
