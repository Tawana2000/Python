# Write a function to generate the first n terms of the Empty square sequence

def empty_square_sequence(n):

    sequence = []

    for i in range(1, n + 1):

        term = ((i + 1) ** 2) - (i ** 2)
        sequence.append(term)

    return sequence

print(empty_square_sequence(5))