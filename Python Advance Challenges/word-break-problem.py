# Given a string and a dictionary of words, determine if the string can be segmented into space-separated words from the dictionary.

def word_break(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is valid
    
    for i in range(1, n + 1):
        for word in wordDict:
            if i >= len(word) and dp[i - len(word)]:
                if s[i - len(word):i] == word:
                    dp[i] = True
                    break
    
    return dp[n]

print(word_break("leetcode", ["leet", "code"])) 
print(word_break("applepen", ["apple", "pen"])) 
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
