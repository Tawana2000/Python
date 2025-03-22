# Write a function to determine the total number of ways that a given integer can be decoded.

def decode_ways(n):
    n = str(n)
    dp = [1, 1] + [0] * (len(n) - 1)
    for i in range(1, len(n)):
        if n[i] != '0': dp[i+1] += dp[i]
        if 10 <= int(n[i-1:i+1]) <= 26: dp[i+1] += dp[i-1]
    return dp[-1]

print(decode_ways(12))