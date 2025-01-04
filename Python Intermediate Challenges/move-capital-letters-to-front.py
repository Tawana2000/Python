# Write a function to move all capital letters in a string to the front

def move_capitals(s):

    capitals = ''.join([char for char in s if char.isupper()])
    non_capitals = ''.join([char for char in s if not char.isupper()])

    return capitals + non_capitals

s = input("Enter a string: ")
print(move_capitals(s))
