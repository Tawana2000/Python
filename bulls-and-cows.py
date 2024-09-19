#Create a Python program to display the number of bulls and cows in a number-guessing game.

def bc(secret, guess):

    bulls, cows = 0, 0

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1

        else:
            if secret[i] in guess:
                cows += 1

    print(f'{bulls}A{cows}B')

secret = '1807'
guess = '7810'
bc(secret, guess)