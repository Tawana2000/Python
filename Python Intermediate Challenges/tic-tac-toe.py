# Write a function to find the cell location of Tic-Tac-Toe Board
# In a game of tic-tac-toe, the board is a 3x3 grid where each cell can be identified by a combination of a letter and a number. 

def get_row_col(cell_str):

    row = {"A": 0, "B":1, "C":2}
    col = int(cell_str[1]) - 1
    return (row[cell_str[0]], col)

print(get_row_col("A1"))
print(get_row_col("B3"))
print(get_row_col("C3"))