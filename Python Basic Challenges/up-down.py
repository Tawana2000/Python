# Write a function to return 'Up' if number is positive, 'Down' if negative and 'Zero' if zero

def up_down(n):
    if n > 0:
        return 'Up'

    elif n == 0:
        return 'Zero'

    else:
        return 'Down'


print(up_down(5))
print(up_down(0))
print(up_down(-21))
