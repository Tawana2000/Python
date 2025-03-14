# Write a function to generate the Number sequence up to a given number

"""
The Number sequence begins with 0 and 1. From the third element onwards, it's built using the following logic:

For even n:
A(n) = A(n/2)

For odd n:
A(n)=A(n/2)+A(n/2+1)

Example Calculation
So the first 7 terms of the sequence are:

A(0) = 0
A(1) = 1
A(2) (even) = A(2/2) = A(1) = 1
A(3) (odd) = A(3/2) + A((3/2) + 1) = A(1) + A(2) = 1 + 1 = 2
A(4) (even) = A(4/2) = A(2) = 1
A(5) (odd) = A(5/2) + A((5/2) + 1) = A(2) + A(3) = 1 + 2 = 3
A(6) (even) = A(6/2) = A(3) = 2
📌 Note: We are taking the floor index for improper divisions like 3/2, 5/2, etc.
"""

def generate_sequence(n):
    seq = [0, 1] 
    for i in range(2, n + 1):
        seq.append(seq[i // 2] if i % 2 == 0 else seq[i // 2] + seq[i // 2 + 1])
    return seq

print(generate_sequence(7))