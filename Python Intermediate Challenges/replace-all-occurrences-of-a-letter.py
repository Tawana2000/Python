# Write a function to replace all occurrence of 'x' in a string
# Replace x with
# 'cks' if it is followed by a vowel
# 'k' if it is followed by a consonant

def replace_x(s):
    vowels = 'aeiou'
    result = []

    for i in range(len(s)):
        if s[i] == 'x':
            if i + 1 < len(s) and s[i + 1] in vowels:
                result.append('cks')
            else:
                result.append('k')
        else:
            result.append(s[i])
    
    return ''.join(result)

text = "example xerox text fixx"
print(replace_x(text))