# Write a function to convert a given string to Spongecase

def to_spongecase(text):

    result = ''
    i = 0

    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                result += char.lower()

            else:
                result += char.upper()

            i += 1
        else:
            result += char
    return result

print(to_spongecase('interviewquestions'))