#Write a function to remove all special characters from a given string

def remove_special(text):

    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return cleaned_text

text = 'Hello@# World!!*.'
print(remove_special(text))