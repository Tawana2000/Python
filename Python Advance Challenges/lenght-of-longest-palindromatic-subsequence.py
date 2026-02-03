# Write a function to find the lenght of the longest palindromatic subsequence in a given string

def longest_palindrome_subsequence(s):

    n = len(s)

    dp = [[0] * n for _ in range(n)]
    

    for i in range(n):
        dp[i][i] = 1
    
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:

                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    

    return dp[0][n - 1]

print(longest_palindrome_subsequence("bbbab")) 
print(longest_palindrome_subsequence("cbbd"))  
print(longest_palindrome_subsequence("a"))
print(longest_palindrome_subsequence("addaber"))
print(longest_palindrome_subsequence(""))       
