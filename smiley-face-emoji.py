# write a function to replace all occurrences of :) in a string with a smiley face emoji

def replace_smiley(text):

    return text.replace(':)', '😊')

input_text = "Hello :) How are you today? :)"
print(replace_smiley(input_text))