# Write a function to play the loves me, loves me not game

def loves_me_not(n):

    result = []

    for i in range(1, n + 1):
        if i % 2 != 0:
            result.append('Loves me')
        else:
            result.append('Loves me not')

    return result

print(loves_me_not(4))