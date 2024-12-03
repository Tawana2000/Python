# Write a function to return the first N vowels from a given string

def first_n_vowels(string, n=4):

    vowels = 'aeiouAEIOU'
    result = []

    for i in string:
        if i in vowels:
            result.append(i)
            if len(result) == n:
                break  # Stop once we have the first `n` vowels

    return result if result else "Not Found"

print(first_n_vowels("Hello, World!")) 
print(first_n_vowels("Ths s n xmpl."))
    