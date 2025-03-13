# Write a function to check if a number is hyperperfect or not

def is_hyperperfect(n):

    d = sum(i for i in range(1, n) if n % i == 0)
    return d > 1 and (n - 1) % (d - 1) == 0

print(is_hyperperfect(7))
print(is_hyperperfect(21))