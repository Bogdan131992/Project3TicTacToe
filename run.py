class TicTacToeGame:
    """
    Initializesa new instance of the TicTacToe class.
    The board is represented as 3x3 grid, initially filed with empty spaces.
    The current player is set to "X" at the game start.
    """
    self.board = [["" for _ in range(3)] for _ in range (3)]
    self.current_player = "X"



def displayWelcomeMessage ():
    """
    Displays a welcome message at the start of the game
    """
    print ("Welcome to the interactive Tic Tac Toe game")

def print_board (self):
    """
    Prints the current state of the game board
    """
    print ("   0   1   2")
    for row in range (3):
        print (f"{row} " + " | ".join (self.board [row]))
        if row < 2:
            print ("  ---+---+---")






def main():
    displayWelcomeMessage()

main()