class Board:
    def __init__(self):
        self.board = [' ',' ',' ',
                      ' ',' ',' ',
                      ' ',' ',' ']
    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
    #if a player selects position n, n-1 index should be updated
    #we use try and except here because: our board list has 9 items. If the user selects 100 as a position, we cannot fill this position in the list and results in an exception.
    def update_board(self,position,type):
        try:
            if self.board[position - 1] == ' ':
               self.board[position - 1] = type
               return True
        
            #if position is already filled, ask user to select another position
            else:
              print('Position already selected. Select another position.')
              return False
        except:
            print('Invalid position, select a valid position')
     #if three symbols appear in a row, returning True   
    def check_winner(self,type):
        if (self.board[0] == type and self.board[1] == type and self.board[2] == type) or \
           (self.board[3] == type and self.board[4] == type and self.board[5] == type) or \
           (self.board[6] == type and self.board[7] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[3] == type and self.board[6] == type) or \
           (self.board[1] == type and self.board[4] == type and self.board[7] == type) or \
           (self.board[2] == type and self.board[5] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[4] == type and self.board[8] == type) or \
           (self.board[2] == type and self.board[4] == type and self.board[6] == type):
           return True
        else:
            return False
          
    #if all fields are selected and there is no winner, it's a draw
    #return True if it's a draw 
    def check_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False

class Player:
    def __init__(self, type):
        self.type = type
        self.name = self.get_name()
    def get_name(self):
        if self.type == 'X':
            name = input('Player selecting X, enter your name: ')
        else:
            name = input('Player selecting O, enter your name: ')
        return name
    
class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_Player = self.player1
    
    #we use try and except here because: If the user enters an invalid position (like strings). So we need to wrap that code inside try..except
    def play(self):
        while True:
            
            try:

                message = f'{self.current_Player.name}, enter the possition (1-9): '
                position = int(input(message))
            #the update_board() method returns True if the selected position is not already filled
                if self.board.update_board(position,self.current_Player.type):
                   self.board.print_board()
                #checking the winner each time after updating the board
                   if self.board.check_winner(self.current_Player.type):
                      print(self.current_Player.name, 'Wins!')
                      break
                #checking draw each time after updating the board
                   elif self.board.check_draw():
                       print('Game is a draw!')
                       break
                #changing current player after board is updated
                else:
                    if self.current_Player == self.player1:
                        self.current_Player = self.player2
                    else:
                        self.current_Player = self.player1
            except:
                print('Invalid input! Enter a number between (1-5).')
        
 
game = Game()
game.play()
