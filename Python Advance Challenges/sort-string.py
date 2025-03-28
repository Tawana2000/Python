# Write a function to rearrange a string in sorted order of alphabets followed by the sum of integers

def rearrage_strings(s):

    sum_digit = 0
    letters = []

    for char in s:
        if char.isdigit():
            sum_digit += int(char)

        else:
            letters.append(char)

    return "".join(sorted(letters)) + (str(sum_digit) if sum_digit > 0 else "")

print(rearrage_strings("dcba4321"))