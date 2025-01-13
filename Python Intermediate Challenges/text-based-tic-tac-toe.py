# Create a simple text_based Tic-Tac-Toe game for two players

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != " " for row in range(3)):
            return True
    if all(board[i][i] == board[0][0] and board[0][0] != " " for i in range(3)):
        return True
    if all(board[i][2 - i] == board[0][2] and board[0][2] !=
