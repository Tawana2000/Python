# Write a function to represent the intensity of an explosion

def explosion_intensity(s):

    result = ""

    for i, char in enumerate(s, start = 1):

        result += char * i

    return result

print(explosion_intensity('Boom'))