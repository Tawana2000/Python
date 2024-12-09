# Write a function to replace 'yt' in 'Python' with a given string

def replace_substring(sub, characters):
    
    result = sub.replace('yt', characters)

    return result

characters = input("Enter the characters to replace 'yt': ")
sub = 'Python'

print(replace_substring(sub, characters))