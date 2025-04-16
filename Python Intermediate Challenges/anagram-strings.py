# Write a function to find if two given words are anagrams and their squares are also anagrams

def anagramic_squares(word1, word2):

    if sorted(word1) != sorted(word2):
        return False
    
    square1 = sorted([ord(char) ** 2 for char in word1])
    square2 = sorted([ord(char) ** 2 for char in word2])
        
    return square1 == square2

print(anagramic_squares('cat', 'tac'))
