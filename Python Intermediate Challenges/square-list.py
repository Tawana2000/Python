# Write a function to generate a list of squares of numbers from 1 to n

def generate_squares(n):

    result = []

    for i in range(1, n + 1):
        result.append(i ** 2)

    return result

print(generate_squares(5))