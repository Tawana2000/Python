# Write a function to return the first N vowels from a given string.

def first_n_vowels(string, n):
    
    vowels = 'aeiouAEIOU'
    result = []

    for i in string:
        if i in vowels:
            result.append(i)
            if len(result) == n:
                break

    return result if result else "Not found"

print(first_n_vowels("Hello World", 3))