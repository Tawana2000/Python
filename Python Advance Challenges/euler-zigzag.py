# Write a function to calculate the nth Euler Zigzag number
# Euler's zigzag numbers (or up/down numbers), denoted E(n), are a sequence of integers that describe the number of permutations of [1, ...., n] that are alternating (or "zig-zagging")

def euler_zigzag(n):

    if n < 0:
        return 0
    if n <= 1:
        return 1
    
    prev2, prev1 = 1, 1
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            prev2, prev1 = prev1, prev1 + prev2

        else:
            prev2, prev1 = prev1, prev1 * 2

    return prev1

print(euler_zigzag(4))
