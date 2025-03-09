# Write a function to check if a number is colossally abundant or not
# A Colossally abundant number is a number for which the sum of its proper divisors is greater than the number itself, and it has more divisors than any smaller number

def is_colossally_abundant(n):

    result = []

    for i in range(1, n):
        if n % i == 0:
            result.append(i)

        if n < sum(result):
            return True
        
    return False

print(is_colossally_abundant(12))