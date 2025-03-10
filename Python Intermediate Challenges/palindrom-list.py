# Write a function to generate a list of palindrome numbers within a given range

def generate_palindromes(start, end):

    result = []
    for i in range(start, end + 1):

        if str(i) == str(i)[::-1]:
            result.append(int(i))

    return result

print(generate_palindromes(10, 100))