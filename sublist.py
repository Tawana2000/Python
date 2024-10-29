# Write a function to create a list that contains 5 identical sublists

def sublists(n):

    return [[n[0]] for _ in range(5)]

n = [3]
print(sublists(n))