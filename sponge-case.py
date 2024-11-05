# Write a function to check if a given string is in spongecase

def sponge_case(text):
    result = ''
    i = 0

    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                result += char.upper()

            else:
                result += char.lower()

            i += 1
        else:
            result += char
    return result

print(sponge_case('My name is Ali!'))