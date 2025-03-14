# Write a function to simulate a game of Rock, Paper, Scissors.

def rock_paper_scissors(player1_choice, player2_choice):

    if player1_choice == 'rock' and player2_choice == 'scissors':
        return "Player 1 wins"
    
    elif player1_choice == 'paper' and player2_choice == 'rock':
        return "player 1 wins"
    
    elif player1_choice == 'scissors' and player2_choice == 'paper':
        return 'player 1 wins'
    
    elif player1_choice == player2_choice:
        return 'Draw'
    
    else:
        return 'Player 2 wins'
    

player1_choice =  input('Player 1 make your selection: "rock", "paper", "scissors " ').strip().lower()
player2_choice = input('Player 2 make your selection: "rock", "paper", "scissors " ').strip().lower()

print(rock_paper_scissors(player1_choice, player2_choice))


# A more efficient way to solve this challange

"""
def rock_paper_scissors(player1_choice, player2_choice):

    outcomes = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if player1_choice == player2_choice:
        return "Draw"
    
    return "Player 1 wins" if outcomes[player1_choice] == player2_choice else "Player 2 wins"

p1 = input('Player 1: rock, paper, scissors? ').strip().lower()
p2 = input('Player 2: rock, paper, scissors? ').strip().lower()

print(rock_paper_scissors(p1, p2))"

"""