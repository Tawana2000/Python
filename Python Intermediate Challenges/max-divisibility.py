# Write a function to find the maximum divisibility score of a number

def max_divisibility_score(n):
    max_score = 0
    best_number = 0

    for i in range(1, n + 1):
        score = sum(i % j == 0 for j in range(1, i + 1))
        if score > max_score:
            max_score = score
            best_number = i

    return best_number, max_score

n = 10
result = max_divisibility_score(n)
print(f"Number with highest divisibility: {result[0]} (Divisors: {result[1]})")



