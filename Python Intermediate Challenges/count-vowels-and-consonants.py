# Write a function that counts the number of vowels and consonants in a given string.

def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = 0
    vowel_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonants += 1
                
    return vowel_count, consonants

vowels, consonants = count_vowels_and_consonants("Hello World!")
print(f"Vowels: {vowels}, Consonants: {consonants}")
