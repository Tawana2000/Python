import random
items = ['rock', 'raper','scissors']

a = input('Player_1: Please make your selection  --> rock, --> paper, --> scissors:\n')
b = random.choice(items)
#b = int(input('Player_2: Please make your selection, 1 ----> Rock, 2 ----> Paper, 3 ----> Scissors:\n'))

while a and b in items:
    if a == b:
        print('Draw')
        break
    elif (a == 'rock' and b == 'paper') or (a == 'scissors' and b == 'paper'):
        print(f'Player_2 won: {b}')
        break
    elif (a == 'paper' and b == 'rock') or (a == 'rock' and b == 'scissors'):
        print('player_1 won')
        break
else:
    print('Please make a valid selection!')

    


