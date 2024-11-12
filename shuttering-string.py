# Write a function to create a shuttering effect on a given word

def shutter_effect(text):

    if len(text) > 2:
        output = f"{text[:2]}... {text[0:2]}... {text}??"

    else:
        output = text

    return output

print(shutter_effect('Hello'))